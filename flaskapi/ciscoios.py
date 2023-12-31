#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparms = {}
        qparms["switchname"] = request.args.get("switchname", "bootstrapped switch")
        qparms["username"] = request.args.get("username", "admin")
        qparms["defaultgateway"] = request.args.get("gateway", "0.0.0.0")
        qparms["switchIP"] = request.args.get("ip", "0.0.0.0")
        qparms["netmask"] = request.args.get("mask", "255.255.255.0")
        qparms["mtusize"] = request.args.get("mtu", "1450")

        return render_template("baseIOS.conf.j2", **qparms)

    except Exception as err:
        return f"Unhanelded excelption {err}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
