#!/usr/bin/python3
"""API Blueprint"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


import api.v1.views.index
import api.v1.views.states
import api.v1.views.cities
import api.v1.views.amenities
import api.v1.views.users
from api.v1.views.places import *
import api.v1.views.places_reviews
