#mongo setup
conn = Connection()
db = conn["event_narwhal"]

#flask setup
app = Flask(__name__)


def validated(user_id):
    sessions[user]= db.users.find("user_id":user_id);

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

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
    app.run()
