import smtplib
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from datetime import datetime

### Email details
WEB_EMAIL = os.environ.get("WEB_EMAIL_ADDRESS")
WEB_EMAIL_PASSWORD = os.environ.get("WEB_EMAIL_PASSWORD")
SMTP_ADDRESS = os.environ.get("WEB_EMAIL_SMTP_ADDRESS")


## Create the Flask app
app = Flask(__name__)

year = datetime.now().year

## Initial the Bootstrap
bootstrap = Bootstrap5(app)


## Initial the Flask Form
# A secret key is required to use CSRF with Flask Form
app.config['SECRET_KEY'] = os.environ.get("FLASK_FORM_SECRET_KEY")


## Forms
# Gender and age finder
class NameForm(FlaskForm):
    name = StringField(label="Given Name (e.g. Peter, Ana, Josh): ", validators=[DataRequired()])
    submit = SubmitField(label="Ok")

# Send message
class SendMessageForm(FlaskForm):
    name = StringField(label="Your name: ", validators=[DataRequired()])
    email = StringField(label="Your email: ", validators=[DataRequired(), Email()])
    message = TextAreaField(label="Your message:", validators=[DataRequired()])
    submit = SubmitField(label="Send message")


## Level 1 routes
# Homepage route
@app.route("/")
@app.route("/<page>")
def home(page="#home"):
    return render_template("Level1/index.html", active_page=page, year=year)

# About route
@app.route("/about")
@app.route("/<page>")
def about(page="about"):
    return render_template("Level1/about.html", active_page=page, year=year)


# Contact Me route
@app.route("/contact_me", methods=["GET", "POST"])
@app.route("/<page>")
def contact(page="contact_me"):

    ## Create the form here
    send_form = SendMessageForm()
    if send_form.validate_on_submit():
        sender_name = send_form.name.data
        sender_email = send_form.email.data
        sender_message = send_form.message.data

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=WEB_EMAIL,
                             password=WEB_EMAIL_PASSWORD)
            connection.sendmail(from_addr=WEB_EMAIL,
                                to_addrs=os.environ.get("MY_EMAIL"),
                                msg=f"Subject: Message from {sender_name} via website contact form.\n\n"
                                    f"Message received from {sender_name} with {sender_email}\n"
                                    f"\nThe message is:\n"
                                    f"\n{sender_message}")

            with smtplib.SMTP(SMTP_ADDRESS) as connection_receipt:
                connection_receipt.starttls()
                connection_receipt.login(user=WEB_EMAIL,
                                        password=WEB_EMAIL_PASSWORD)
                connection_receipt.sendmail(from_addr=WEB_EMAIL,
                                    to_addrs=sender_email,
                                    msg=f"Subject: The message has been sent to Istvan.\n\n"
                                        f"\nThe message you sent:\n"
                                        f"\n{sender_message}")

        send_form.name.data = ""
        send_form.email.data = ""
        send_form.message.data = (f"The message has been sent\n"
                                  f"You will get a copy of your message shortly.")

    return render_template("Level1/contact.html", active_page=page, year=year, form=send_form)


## Level 2 routes

# Note Application
@app.route("/note_application", methods=["GET", "POST"])
@app.route("/<page>")
def note_app(page="note_application"):
    return render_template("Level2/note_app.html",
                           active_page=page, year=year)


# Tic Tac Toe Game
@app.route("/tic_tac_toe", methods=["GET", "POST"])
@app.route("/<page>")
def tic_tac_toe(page="tic_tac_toe"):
    return render_template("Level2/tic_tac_toe.html",
                           active_page=page, year=year)


# Image Watermarking Application
@app.route("/image_watermarking_application", methods=["GET", "POST"])
@app.route("/<page>")
def image_watermarking_app(page="image_watermarking_application"):
    return render_template("Level2/image_watermarking_app.html",
                           active_page=page, year=year)


# Portfolio Website
@app.route("/portfolio_website", methods=["GET", "POST"])
@app.route("/<page>")
def portfolio_website(page="portfolio_website"):
    return render_template("Level2/portfolio_website.html",
                           active_page=page, year=year)


## Run the server with debug mode
if __name__ == "__main__":
    app.run(debug=True)
