#!/usr/bin/python3
"""API Blueprint"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from .index import *
from .states import *
from .cities import *
from .amenities import *
from .users import *
from .places import *
