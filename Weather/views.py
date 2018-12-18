from django.shortcuts import render, HttpResponse
import requests


# Create your views here.
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a5ec053718588afe7c9be31031631cc6'
    city = 'delhi'
    
    

    response = requests.get(url.format(city)).json()

    city_weather = {
            'city': city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon']
        }

    ref = {'city_weather' : city_weather}
    
    if request.method == 'POST':
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a5ec053718588afe7c9be31031631cc6'
        city = request.POST.get('city')

    


        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature' : response['main']['temp'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon']
        }

        ref = {'city_weather' : city_weather}
    
    return render(request, 'Weather/base.html', ref)

