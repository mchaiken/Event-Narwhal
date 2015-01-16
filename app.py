from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection
import database_actions
#pip install facebook-sdk
import facebook
import json
#http://stackoverflow.com/questions/10693630/how-to-pass-a-boolean-from-javascript-to-python use this
#for the js to python transfer

#fb setup
#graph = facebook.GraphAPI(oauth_access_token)

#mongo setup
conn = Connection()
db = conn["event_narwhal"]


#flask setup
app = Flask(__name__)

def validated(user_id):
    sessions[user]= db.users.find("user_id:"+user_id)


@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def home():
    if 'user' not in session:
        return render_template("home.html")
    return render_template("myevents.html", events=database_actions.get_events(session['user']))

@app.route("/new")
def new_event():
    if 'user' not in session:
        return redirect('/')
    if request_method == "POST":
        database_actions.add_event(name=request.form["name"]) #this isn't done, but just a placeholder
    return render_template('newevent.html',facebook_events=["event1","event2"])

@app.route("/events/<event_index>")
def event(event_index):
    if 'user' not in session:
        redirect("/")
    return render_template("event.html",event=database_actions.get_event(session["user"],event_index))

#logout button on other pages will redirect to this
@app.route("/logout")
def logout():
    #log user out
    #page will have button to return to login page
    session.pop('user',None)
    return render_template("logout.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key=open("secret_key.txt").read()
    app.run(host="149.89.150.1")
