import googlemaps
from datetime import datetime

def my_function(first_address,second_address):
    now = datetime.now()

    # API
    gmaps = googlemaps.Client(key='Your API Key')

    # CONVERT ADDRESS TO COORDINATE
    geocode1 = gmaps.geocode(first_address)
    geocode2 = gmaps.geocode(second_address)

    geocode1_lat = geocode1[0]['geometry']['location']['lat']
    geocode1_lng = geocode1[0]['geometry']['location']['lng']
    geocode1_lat = str(geocode1_lat)
    geocode1_lng = str(geocode1_lng)
    coordinate = geocode1_lat + ", " + geocode1_lng

    geocode2_lat = geocode2[0]['geometry']['location']['lat']
    geocode2_lng = geocode2[0]['geometry']['location']['lng']
    geocode2_lng = str(geocode2_lng)
    geocode2_lat = str(geocode2_lat)
    coordinate2 = geocode2_lat + ", " + geocode2_lng

    directions_result = gmaps.directions(coordinate, coordinate2, mode="driving", alternatives=None, waypoints=None,
                                         optimize_waypoints=False, avoid=None, language=None, units=None, region=None,
                                         departure_time=now, arrival_time=None)
    return "Distance: "+directions_result[0]['legs'][0]['distance']['text']+"\n"+"Duration: "+directions_result[0]['legs'][0]['duration']['text']

