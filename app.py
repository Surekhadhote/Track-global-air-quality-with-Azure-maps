import os, json
from flask import Flask, render_template, request
import requests

# Load the Azure Maps key from the .env file
MAP_KEY = os.environ["MAP_KEY"]

# Initialize the Flask app
app = Flask(__name__)

# Handle requests to the root of the web site, returning the home page
@app.route("/")
def home():
    # Create data for the home page to pass the maps key
    data = { "map_key" : MAP_KEY }
    # Return the rendered HTML page
    return render_template("home.html", data = data)
