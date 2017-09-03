"""
Haversine formula in python
"""
import math

EARTH_RADIUS = 6371


def distance(origin, destination):
    """
    Gets distance between two points
    :param origin: a tuple of latitude, longitude
    :param destination: a tuple of latitude, longitude
    :return:
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) \
        * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = EARTH_RADIUS * c

    return d
