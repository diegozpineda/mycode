#!/usr/bin/env python3
''' Flask server for coingecko app'''

from flask import Flask
from flask import render_template
import crypto_coingecko

app = Flask(__name__)

@app.route("/")
def index():
    market_data = crypto_coingecko.get_marketdata()

    return render_template("week2site.html", market_data=market_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)