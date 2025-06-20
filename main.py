from flask import Flask, render_template, request, url_for, redirect
import requests
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

## Create the Flask app
app = Flask(__name__)

year = datetime.now().year

## Initial the Bootstrap
bootstrap = Bootstrap5(app)


## Initial the Flask Form
# A secret key is required to use CSRF with Flask Form
app.config['SECRET_KEY'] = "Test1234"


# Forms
class NameForm(FlaskForm):
    name = StringField(label="Given Name (e.g. Peter, Ana, Josh): ", validators=[DataRequired()])
    submit = SubmitField(label="Ok")

## Level 1 routes
# Homepage route
@app.route("/")
@app.route("/<page>")
def home(page="home"):
    return render_template("Level1/index.html", active_page=page, year=year)


# About route
@app.route("/about")
@app.route("/<page>")
def about(page="about"):
    return render_template("Level1/about.html", active_page=page, year=year)


# Projects route
@app.route("/projects")
@app.route("/<page>")
def projects(page="projects"):
    return render_template("Level1/projects.html", active_page=page, year=year)


# Contact Me route
@app.route("/contact_me")
@app.route("/<page>")
def contact(page="contact_me"):
    return render_template("Level1/contact.html", active_page=page, year=year)


## Level 2 routes
# Projects routes
# Python Scripting - Text to Morse Code Converter
@app.route("/project/text_to_morse", methods=["GET", "POST"])
@app.route("/project/<page>")
def text_to_morse(page="text_to_morse"):
    return render_template("Level2/text_to_morse.html",
                           active_page=page, year=year)

# Python Scripting - Tic Tac Toe
@app.route("/project/tic_tac_toe", methods=["GET", "POST"])
@app.route("/project/<page>")
def tic_tac_toe(page="tic_tac_toe"):
    return render_template("Level2/tic_tac_toe.html",
                           active_page=page, year=year)


# HTTP Requests and APIs route - Gender and age finder
@app.route("/project/gender_and_age_finder", methods=["GET", "POST"])
@app.route("/project/<page>")
def gender_age(page="gender_and_age_finder"):
    name_form = NameForm()
    user_input = "Type a name for result"
    gender = "Press Ok for result"
    age = "Press Ok for result"
    if name_form.validate_on_submit():
        user_input = name_form.name.data
        gender_url = f"https://api.genderize.io?name={user_input}"
        response_gender = requests.get(gender_url)
        gender_json = response_gender.json()
        gender = gender_json["gender"]

        age_url = f"https://api.agify.io?name={user_input}"
        response_age = requests.get(age_url)
        age_json = response_age.json()
        age = age_json["age"]

        return render_template("/Level2/gender_and_age_finder.html",
                               active_page=page, year=year,
                               form=name_form, name=user_input, gender=gender, age=age)

    return render_template("Level2/gender_and_age_finder.html",
                           active_page=page, year=year,
                           form=name_form, name=user_input, gender=gender, age=age)

## Run the server with debug mode
if __name__ == "__main__":
    app.run(debug=True)
