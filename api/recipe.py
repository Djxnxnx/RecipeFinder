import json
from flask import Blueprint, request, jsonify
import requests
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.users import User

recipe_api = Blueprint('recipe_api', __name__,
                   url_prefix='/api/recipes')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(recipe_api)

class UserAPI:        
    class _CRUD(Resource):  # User API operation for Create, Read.  THe Update, Delete methods need to be implemeented
        def get(self, ingredients): # Create method
            api_key = '84cfe45628de456c87a13a80b76f5bd8'  # Replace with your Spoonacular API key
            url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients=" + ingredients
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return jsonify(data)
            else:
                #return jsonify({"error": "Failed to fetch recipes."}), response.status_code
             return {'message': f'hello'}, 400
        
    # class _Security(Resource):

    #     def post(self):
    #         ''' Read data for json body '''
    #         body = request.get_json()
            
    #         ''' Get Data '''
    #         uid = body.get('uid')
    #         if uid is None or len(uid) < 2:
    #             return {'message': f'User ID is missing, or is less than 2 characters'}, 400
    #         password = body.get('password')
            
    #         ''' Find user '''
    #         user = User.query.filter_by(_uid=uid).first()
    #         if user is None or not user.is_password(password):
    #             return {'message': f"Invalid user id or password"}, 400
            
    #         ''' authenticated user '''
    #         return jsonify(user.read())

            

    # building RESTapi endpoint
    #api.add_resource(_CRUD, '/')
    #api.add_resource(_Security, '/authenticate')
    api.add_resource(_CRUD, '/getrecipes/<ingredients>')
    