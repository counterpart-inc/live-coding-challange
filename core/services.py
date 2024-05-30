from datetime import datetime
import logging

from haversine import haversine
import requests

from core.models import SearchResult


logger = logging.getLogger(__name__)


class EarthquakeService:
    
    # TODO
    # Build the service

    def find_nearest_earthquake(self, earthquakes, data):
        """
        Finds the nearest earthquake to a given data (city, start_date and end_date).
        """
        city = data["city"]
        earthquake_data = {
            "city": city,
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "earthquake_date": None,
            "title": None,
        }

        nearest_distance = float("inf")
        for earthquake in earthquakes:
            try:
                eq_lat = earthquake["geometry"]["coordinates"][1]
                eq_long = earthquake["geometry"]["coordinates"][0]
                distance = haversine((eq_lat, eq_long), (city.lat, city.long))

                if distance < nearest_distance:
                    nearest_distance = distance
                    timestamp = earthquake["properties"]["time"]
                    earthquake_data["earthquake_date"] = datetime.fromtimestamp(
                        timestamp / 1000
                    ).date()
                    earthquake_data["title"] = earthquake["properties"]["title"]
            except (KeyError, ValueError) as e:
                logger.error(f"Error when processing earthquake data: {e}")

        return earthquake_data
