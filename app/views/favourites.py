from flask import render_template, request, redirect, make_response

from app import app
from app.models import dynamodb_favourites

def get_favourites(username: str):
    
    favourites = dynamodb_favourites.get_favourites(username) 
    return favourites

def add_favourite(favourites: set):
    favourites.add()
