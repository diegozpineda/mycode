#!/usr/bin/python3
'''First Flask App'''

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return f"Hello Admin" 

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty}" 

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with value of admin
    if name == "admin":
        # 302 redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # 302 redirect to /guest/<guesty>
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the app

    
