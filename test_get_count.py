#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City

all_objects_count = storage.count()
state_objects_count = storage.count(State)

print(f"All objects: {all_objects_count}")
print(f"State objects: {state_objects_count}")

states = storage.all(State)
print(f"States: {states}")

first_state_id = list(states.values())[0].id
city_objects_count = storage.count(City, first_state_id)

print(f"City objects for the first state: {city_objects_count}")
