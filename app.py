from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection
import database_actions
#pip install facebook-sdk
import facebook
import json
import FB


#fb setup
FBAppID = "1556299804628530"
FBAppSecret = "caf5c0f2cd36a15c61949d9991170d0d"
#http://stackoverflow.com/questions/10693630/how-to-pass-a-boolean-from-javascript-to-python use this
#for the js to python transfer




   
#mongo setup
conn = Connection()
db = conn["event_narwhal"]


#flask setup
app = Flask( __name__ )


def validated( user_id ):
        sessions[user] = db.users.find( "user_id:" + user_id )


@app.route( "/", methods = ["GET", "POST"] )
@app.route( "/home", methods = ["GET", "POST"] )
def home():
        if 'user' not in session:
                cookie = facebook.get_user_from_cookie( request.cookies, FBAppID, FBAppSecret )
                print cookie
                if cookie != None:
                        session["token"] = cookie["access_token"]
                        session["user"] = FB.getID( session["token"] )
                        session["name"] =FB.getName(session["token"])
                        if database_actions.isRegistered(session["user"]):
                            database_actions.login_user(session["user"])
                        else:
                            database_actions.register_user(session["name"],session["user"])

                        #return redirect( "/" )
                return render_template( "home.html" )
        return render_template( "my_events.html", events=database_actions.get_events(session["user"]) )


@app.route( "/new" )
def new_event():
        if 'user' not in session:
                return redirect('/')
        #if request_method == "POST":
        #   database_actions.add_event(name=request.form["name"]) #this isn't done, but just a placeholder
        return render_template( 'settings.html', facebook_events=FB.getAllEvents( session["token"] ), events=database_actions.get_events( session["user"] ) )


@app.route( "/event/<event_index>" )
def event( event_index ):
        if 'user' not in session:
                return redirect( "/" )
        return render_template( "event.html", event=database_actions.get_event(session["user"], event_index), events=database_actions.get_events(session["user"]) )


#logout button on other pages will redirect to this
@app.route( "/logout" )
def logout():

#        print FB.getGuests(session["token"], getAllEvents(session["token"])[0])
        print FB.getGuests(session["token"], "760519097373077")

        #log user out
        #page will have button to return to login page
        session.pop( 'user', None )
        return render_template( "logout.html" )
#logout button on other pages will redirect to this


@app.route( "/login" )
def login():
        #this is temporary until we have fb working
        #page will have button to return to login page
        #session['user'] = 123456789
        return redirect( "/" )


if __name__ == "__main__":
        app.debug = True
        app.secret_key = open( "secret_key.txt" ).read()
        app.run( host="149.89.150.1" )
#        app.run()
