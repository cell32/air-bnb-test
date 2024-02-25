# data_collector.py

import os
import traceback
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def retrieve_airbnb_data(num_bedrooms, country):
    try:
        # MongoDB connection details
        # connection_string = os.getenv("MONGODB_URI")
        database_name = "sample_airbnb"
        collection_name = "listingsAndReviews"

        # Connect to MongoDB Atlas
        # client = MongoClient(connection_string)
        client = MongoClient("mongodb+srv://cell32:OJzViDMsp75xYXVt@cluster0.fz0r2ef.mongodb.net/?retryWrites=true&w=majority")
        db = client[database_name]
        collection = db[collection_name]

        # Query MongoDB based on user input
        query = {
            "bedrooms": {"$eq": int(num_bedrooms)},
            "address.country": country
        }

        result = list(collection.find(query))

        # Close the MongoDB connection
        client.close()

        return result
     
    except Exception as e:
        print("Exception during MongoDB connection:")
        print(str(e))
        print(traceback.format_exc())  # Print the traceback for more details
        return []
    
