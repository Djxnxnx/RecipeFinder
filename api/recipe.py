from typing import Any
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.jokes import *

recipe_api = Blueprint('joke_api', __name__,
                   url_prefix='/api/recipes')

api = Api(recipe_api)

class recipe:

    class _getrecipes(Resource):
        def get(self):
            api_key = '84cfe45628de456c87a13a80b76f5bd8'  # Replace with your Spoonacular API key
            ingredients = requests.args.get('ingredients')
            if not ingredients:
                return jsonify({"error": "Please provide ingredients as a query parameter."}), 400

            url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)
            else:
                return jsonify({"error": "Failed to fetch recipes."}), response.status_code
            
    api.add_resource(_getrecipes, '/getrecipes')
