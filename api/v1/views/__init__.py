#!/usr/bin/python3
"""API Blueprint"""
from flask import Blueprint
from functools import wraps

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


def import_deferred(imp):
    @wraps(imp)
    def wrapper(*args, **kwargs):
        return imp(*args, **kwargs)
    return wrapper


@import_deferred
def import_views():
    from .index import *
    from .states import *


import_views()
