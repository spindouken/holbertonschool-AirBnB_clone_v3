#!/usr/bin/python3
"""MTV Cribs edition of Place API views"""
from flask import jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def show_me_all_the_cribs(city_id):
    """
    Show me all the cribs...
    Endpoint to retrieve all Place objects of a City
    (Uses city_id to retrieve city object and get all associated places)
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    cribs = [crib.to_dict() for crib in city.places]
    return jsonify(cribs)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def one_single(place_id):
    """
    A single dope crib...
    Endpoint to retrieve a specific Place object
    (Uses the place_id to fetch the associated Place object)
    """
    crib = storage.get(Place, place_id)
    if crib is None:
        abort(404)
    return jsonify(crib.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def we_dont_need_no_water(place_id):
    """
    let the place burn...
    Endpoint to delete a specific Place object
    (Uses the place_id to fetch the associated
    Place object and delete it from storage)
    """
    crib = storage.get(Place, place_id)
    if crib is None:
        abort(404)
    storage.delete(crib)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def bobby_builder(city_id):
    """
    Show all the JSON crib data...
    Endpoint to create a new Place object
    (Uses the city_id to associate the new Place object with a City,
    Validates the JSON request data,
    and creates a new Place object accordingly)
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    crib_data = request.get_json()
    if crib_data is None:
