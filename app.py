from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["even_narwhal"]



def validated(user_id):
    sessions[user]= db.users.find("user_id:"+user_id);

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")
@app.route("/register", methods = ["GET", "POST"])
def register():
    return render_template("login.html")
#logout button on other pages will redirect to this
@app.route("/logout")
def logout():
    #log user out
    #page will have button to return to login page
    session.pop('user',None)
    return render_template("logout.html")

@app.route("/foodresults", method=["GET","POST"])
def foodresults():
    if request.method=="GET":
        attribute= request.args.get("mymenu")
        search = request.args.get("search")
            if attribute== "ingredients":   
                search= search.split(",")
    #how do I seperate the request method from the drop down from the search bar?
        results=yummly.getResults(attribute,search)
    return render_temple("foodresults.html", attribute=attribute, results= results)    




if __name__ == "__main__":
    app.debug = True
    app.secret_key=open("secret_key.txt").read()
    app.run()
