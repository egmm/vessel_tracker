# Vessel/Ship tracker application
It keeps track of your vessel/ship around the world

## Requirements
-Python 3.6 or later
-Docker

## How to run
In the main directory, start the docker containers:
``
docker-compose up

``

Once the service is up, prepopulate the database:
``
docker exec -it vessel_ship_track_web_1 python launch.py

``
Now you should have the API running local on port 8000.

## Future releases
- Create the UI in React and use the kepler.gl framework to
make sick maps!