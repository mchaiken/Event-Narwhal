from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection
import database_actions
#pip install facebook-sdk
import facebook
import json
import FB
import yummly
import urllib2, json
def getResults( attribute, search ):
    #attribute = if it is a holiday, cusine, or ingredient
    #search = their actual input
    #need to take into account if their search is not a real holiday
    url = ""
    if attribute == "holiday":
        url = "http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e&q=&allowedHoliday[]=holiday^holiday-" + search.lower()
    elif attribute == "cuisine":
        url = "http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e&q=&allowedCusine[]=cuisine^cuisine-" + search.lower()
    else:
        url = "http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"
        for ingredient in search:
                if ingredient[0] == " ":
                    ingredient = ingredient[1:]
                    url += "&allowedIngredient[]=" + ingredient.lower()
    request = urllib2.urlopen( url )
    result = request.read()
    #print url
    return json.loads( result )


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
                                print "registering "
                                database_actions.register_user(session["name"],session["user"])

                        #return redirect( "/" )
                return render_template( "home.html" )
        return render_template( "my_events.html", events=database_actions.get_events(session["user"]) )



@app.route( "/new", methods = ["GET", "POST"] )
def new_event():

        try:
                if 'user' not in session:
                        return redirect('/')
                return render_template( 'create.html', facebook_events=FB.getAllEvents( session["token"] ), events=database_actions.get_events( session["user"] ) )
        except:
                session.pop("user")
                return redirect("/")



@app.route( "/set", methods = ["GET", "POST"] )
def set():
        try:
                if 'user' not in session:
                        return redirect('/')
                elif request.method == "POST":
                    ID = request.form["fb_id"]
                    token = session["token"]
                    description = FB.getDescription(token, ID)
                    date = FB.getStartTime(token, ID)
                    location = FB.getLocation(token, ID)
                    attending = FB.getAttending(token, ID)
                    maybe =  FB.getMaybe(token, ID)
                    declined = FB.getDeclined(token, ID)
                    not_responded = FB.getUnknown(token, ID)
                    print database_actions.add_event(session["user"],request.form["name"],request.form["theme"],ID, description, date, location, attending, declined, maybe, not_responded) #this isn't done, but just a placeholder
                    return render_template( 'set.html', events=database_actions.get_events( session["user"] ) )
                return redirect("/new")
        except:
                session.pop("user")
                return redirect("/")



@app.route( "/event/<event_index>" )
def event( event_index ):
        if 'user' not in session:
                return redirect( "/" )
        return render_template( "event.html", event=database_actions.get_event(session["user"], event_index), events=database_actions.get_events(session["user"]) )


#logout button on other pages will redirect to this
@app.route( "/logout" )
def logout():
        cookie = facebook.get_user_from_cookie( request.cookies, FBAppID, FBAppSecret )
        print cookie
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




@app.route( "/8tracks", methods = ["GET", "POST"] )
def eighttracks():
    if 'user' not in session:
        return redirect('/')
    
    return render_template( 'search.html',placeholder="Search 8tracks for music...")





@app.route( "/yummly", methods = ["GET", "POST"] )
def yummly():
    if 'user' not in session:
        return redirect('/')
    if request.args.get("query") != None:
        results= getResults(request.args.get("type"),request.args.get("query"))["matches"]
    else:
        results = None
    print results
    return render_template( 'search.html',placeholder="Search yummly for recipies...",results=results)





if __name__ == "__main__":
        app.debug = True
        app.secret_key = open( "secret_key.txt" ).read()
        app.run( host="149.89.150.1")
        #        app.run()
