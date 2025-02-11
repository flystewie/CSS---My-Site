import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

# Registrants = {}



# name = request.form.get("name")
# if not name:
#     return render_template(message="Missing name")

# Remember registrant
# REGISTRANTS[name] = sport

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
         name = request.form.get("name")
         month = request.form.get("month")
         day = request.form.get("day")
        # TODO: Add the user's entry into the database
         db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

         return redirect("/")
        #   name = request.form.get("name", "world")
        #   return render_template("index.html", name=name)

    else:
        registrants = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", registrants=registrants)
        # TODO: Display the entries in the database on index.html

        # return render_template("index.html")





