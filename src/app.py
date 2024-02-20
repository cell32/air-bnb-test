#!/usr/bin/env python3
	
from flask import Flask, render_template, request
	
app = Flask(__name__)
	
@app.route("/")
def main():
    return render_template("login.html")

	
@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_name = request.form.get("user_input", "")
    input_password = request.form.get("user_password", "")
    return "You entered: " + input_name, input_password



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
