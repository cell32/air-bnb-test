#!/usr/bin/env python3
	
import os
from flask import Flask, redirect, render_template, request, url_for, session
from scripts.data_collector import retrieve_airbnb_data
from scripts.data_modifier import see_highest_ranking_data
from flask_sqlalchemy import SQLAlchemy
from bson.decimal128 import Decimal128
from dotenv import load_dotenv

load_dotenv()
	
app = Flask(__name__)

# Setting up secret key to use session variables and use 'country' input value to be used in another route 
session_secret_key_str = os.getenv('session_secret_key')
session_secret_key_bytes = session_secret_key_str.encode('utf-8')

app.secret_key = session_secret_key_bytes


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Users  model
class Users(db.Model):
    __tablename__ = 'Users'
    id=db.Column("User_ID", db.Integer, primary_key=True)
    listing_url=db.Column(db.String(255))
    name=db.Column(db.String(255))
    city=db.Column(db.String(255))
    bedrooms=db.Column(db.Integer)
    beds=db.Column(db.Integer)
    accommodates=db.Column(db.Integer)
    bathrooms=db.Column(db.Numeric, nullable=True, default=None)
    review_score=db.Column(db.Integer)

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
    session['country'] = country  # Store country in session variables. secret key is needed to use session.

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
            city=item.get('address', {}).get('suburb', ''),
            bedrooms=item.get('bedrooms', 0),
            beds=item.get('beds', 0),
            accommodates=item.get('accommodates', 0),
            bathrooms=item.get('bathrooms', 0.0),
            review_score=item.get('review_scores', {}).get('review_scores_rating', 0)
        )
        db.session.add(user)

    ## Commit changes to the database
    db.session.commit()    

    # You can do something with the result, like passing it to a template
    return render_template("result.html", result=result, country=country)

@app.route('/see_highest_ranking', methods=['POST'])
def see_highest_ranking():
    country =  session.get('country')
    try:
        # Call the function from data_modifier.py
        filtered_rows = see_highest_ranking_data()

        return render_template("dmodified.html", highest_rankings=filtered_rows, country=country)

    except Exception as e:
        print("Exception during see_highest_ranking_route:", e)
        return "An error occurred"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
