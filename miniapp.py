#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("logout.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
<<<<<<< Updated upstream
    #app.run(host="149.89.150.1", port=1639)
    app.run()
=======
    app.run()
#app.run(host="149.89.150.1", port=1639)
>>>>>>> Stashed changes
