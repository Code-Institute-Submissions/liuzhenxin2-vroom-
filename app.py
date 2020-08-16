from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from dotenv import load_dotenv
import datetime

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')

MONGO_URI = os.environ.get('MONGO_URI')

@app.route("/")
def show_index():
    return render_template("index.template.html")


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)