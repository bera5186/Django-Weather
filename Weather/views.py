from django.shortcuts import render, HttpResponse
import requests
from geopy.geocoders import Nominatim
from .map import createMap

# Create your views here.
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a5ec053718588afe7c9be31031631cc6'
    city = 'delhi'
    
    """ The Localtion Map Stuff """
    geolocator = Nominatim(user_agent="Weather", timeout=3)
    location = geolocator.geocode(city)
    
    """ Creating map.html """
    createMap(location.latitude, location.longitude, city)

    response = requests.get(url.format(city)).json()

    city_weather = {
            'city': city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'lat' : location.latitude,
            'long' : location.longitude,
        }

    ref = {'city_weather' : city_weather}
    
    if request.method == 'POST':
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a5ec053718588afe7c9be31031631cc6'
        city = request.POST.get('city')

        """ The Localtion Map Stuff """
        geolocator = Nominatim(user_agent="Weather", timeout=3)
        location = geolocator.geocode(city)

        """ Creating map.html """
        createMap(location.latitude, location.longitude, city)


        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'lat' : location.latitude,
            'long' : location.longitude,
        }

        ref = {'city_weather' : city_weather}
    
    return render(request, 'Weather/base.html', ref)

