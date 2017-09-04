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


def calculate_initial_compass_bearing(origin, destination):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    if (type(origin) != tuple) or (type(destination) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(origin[0])
    lat2 = math.radians(destination[0])

    diff_long = math.radians(destination[1] - origin[1])

    x = math.sin(diff_long) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diff_long))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def speed(point_distance, time):
    """
    Returns the speed an object travels between two points
    :param point_distance: Distance in meters
    :param time: Time in seconds
    :return:
    """
    if point_distance != 0.0:
        object_speed = (distance/time) * 3.6
        object_speed = math.ceil(object_speed * 100) / 100
    else:
        object_speed = "Inaccurate Values Found(Distance: {}, Time: {})".format(point_distance, time)
    return object_speed
