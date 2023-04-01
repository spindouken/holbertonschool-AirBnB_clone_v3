#!/usr/bin/python3
"""documentation yaya"""
from api.v1.views import app_views
from flask import Response
from json import dumps


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Return API status"""
    return Response(dumps({"status": "OK"}), content_type='application/json')
