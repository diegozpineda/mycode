#!/usr/bin/python3
'''First Flask App'''

from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name):
    return f"Hello {name}" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the app

    
