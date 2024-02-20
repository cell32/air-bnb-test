#!/usr/bin/env python3
	
import os
from flask import Flask, redirect, render_template, request, url_for
from scripts.data_collector import retrieve_airbnb_data
from flask_sqlalchemy import SQLAlchemy
from bson.decimal128 import Decimal128
	
app = Flask(__name__)
	
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



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
