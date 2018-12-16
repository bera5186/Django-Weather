import os
import folium

def createMap(latitude, longitude, cityName):
    
    location = []
    location.append(latitude)
    location.append(longitude)
    
    mapObject = folium.Map(location=location, max_zoom=15)
    folium.Marker(
        location,
        popup='<strong>'+ cityName +'</strong>',
        tooltip= 'Click'
    ).add_to(mapObject)
    
    os.chdir('/home/rahul/Programming/Python/Django/WeatherApp/Weather/templates/Weather')
    mapObject.save('map.html')


