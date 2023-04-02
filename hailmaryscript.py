#!/usr/bin/python3

import models
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review

# Create Amenity objects
amenity1 = Amenity(name="Free Wi-Fi")
amenity2 = Amenity(name="Swimming Pool")

# Create State objects
state1 = State(name="California")
state2 = State(name="New York")

# Create City objects
city1 = City(name="Los Angeles", state_id=state1.id)
city2 = City(name="San Francisco", state_id=state1.id)
city3 = City(name="New York City", state_id=state2.id)
city4 = City(name="Buffalo", state_id=state2.id)

# Create User objects
user1 = User(email="john@example.com", password="johnpass", first_name="John", last_name="Doe")
user2 = User(email="jane@example.com", password="janepass", first_name="Jane", last_name="Doe")

# Create Place objects
place1 = Place(city_id=city1.id, user_id=user1.id, name="Amazing LA Apartment", description="Modern apartment in downtown LA", number_rooms=2, number_bathrooms=2, max_guest=4, price_by_night=150, latitude=34.052235, longitude=-118.243683)
place2 = Place(city_id=city2.id, user_id=user1.id, name="Cozy SF Studio", description="Cozy studio in the heart of San Francisco", number_rooms=1, number_bathrooms=1, max_guest=2, price_by_night=100, latitude=37.7749, longitude=-122.419416)
place3 = Place(city_id=city3.id, user_id=user2.id, name="Luxury NYC Penthouse", description="Luxurious penthouse in the heart of NYC", number_rooms=3, number_bathrooms=3, max_guest=6, price_by_night=500, latitude=40.712776, longitude=-74.005974)
place4 = Place(city_id=city4.id, user_id=user2.id, name="Buffalo House", description="Charming house in Buffalo", number_rooms=4, number_bathrooms=2, max_guest=8, price_by_night=200, latitude=42.886448, longitude=-78.878372)

# Create Review objects
review1 = Review(place_id=place1.id, user_id=user1.id, text="Great place! Loved staying here.")
review2 = Review(place_id=place2.id, user_id=user1.id, text="Fantastic location and cozy space!")
review3 = Review(place_id=place3.id, user_id=user2.id, text="The penthouse was amazing, and the view was incredible!")
review4 = Review(place_id=place4.id, user_id=user2.id, text="The house was spacious and perfect for our family trip.")
review5 = Review(place_id=place1.id, user_id=user2.id, text="Had a great time at the LA apartment, highly recommended!")
review6 = Review(place_id=place3.id, user_id=user1.id, text="The NYC penthouse was a dream, would stay again in a heartbeat!")

# Save objects to the storage
for obj in [amenity1, amenity2, state1, state2, city1, city2, city3, city4, user1, user2, place1, place2, place3, place4, review1, review2, review3, review4, review5, review6]:
    obj.save()

print("Objects created and saved successfully!")
