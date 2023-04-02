#!/usr/bin/python3
"""API Blueprint"""
from flask import Blueprint
from .index import *
from .states import *
from .cities import *


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
