#!/usr/bin/env python3
	
import os
from flask import Flask, redirect, render_template, request, url_for
from scripts.data_collector import retrieve_airbnb_data
from flask_sqlalchemy import SQLAlchemy
from bson.decimal128 import Decimal128
	
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Users  model
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column("User_ID", db.Integer, primary_key=True)
    listing_url = db.Column(db.String(255))
    name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    beds = db.Column(db.Integer)
    accommodates = db.Column(db.Integer)
    bathrooms = db.Column(db.Numeric, nullable=True, default=None)

# Create all tables if they do not exist
with app.app_context():
    db.create_all()


@app.route("/")
def main():
    return render_template("login.html")

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_name = request.form.get("user_input", "")
    input_password = request.form.get("user_password", "")
    return redirect(url_for("show_choices", input_name=input_name))

@app.route("/show_choices/<input_name>", methods=["GET", "POST"])
def show_choices(input_name):
    country = request.form.get("country", "")
    return render_template("choices.html", input_name=input_name, country=country)

@app.route("/exit")
def exit():
    return redirect(url_for("main"))

@app.route("/retrieve_airbnb_data", methods=["POST"])
def retrieve_data():
    num_bedrooms = request.form.get("num_bedrooms", 0)
    country = request.form.get("country", "")

    # Call the function from data_collector.py
    result = retrieve_airbnb_data(num_bedrooms, country)


    ## Convert Decimal128 to float
    for item in result:
        for key, value in item.items():
            if isinstance(value, Decimal128):
                item[key] = float(str(value))

    ## Save data to local database using User model
    for item in result:
        user = Users(
            listing_url=item.get('listing_url', ''),            
            name=item.get('name', ''),
            city=item.get('city', ''),
            bedrooms=item.get('bedrooms', 0),
            beds=item.get('beds', 0),
            accommodates=item.get('accommodates', 0),
            bathrooms=item.get('bathrooms', 0.0)
        )
        db.session.add(user)

    ## Commit changes to the database
    db.session.commit()    

    # You can do something with the result, like passing it to a template
    return render_template("result.html", result=result, country=country)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
