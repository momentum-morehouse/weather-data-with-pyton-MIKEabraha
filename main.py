import requests

# If you want to use classes
# class Place:
# would have attributes lat, long, name,
# Would be like a card in blackjack and the place_list would be like a deck

# class WeatherReport
# place, temp, precip

city_list = [
(52.379446, 4.893729, "Amsterdam"),
(9.01133, 38.44585, "Gerji"),
(14.10379, 38.53199, "Adwa"),
(14.07560, 38.43091, "Axum"),
(38.973059, -76.996397, "Takoma"),
(39.151081, -77.070553, "Olney"),
(43.640881, -79.354611, "Toronto"),
(38.919695, -77.029694, "DC")]

def climate(locations):
    climate_data_packet = {}
    for location in locations:
        url = "https://api.climacell.co/v3/weather/realtime"
        payload = {
        "apikey":"2M4OSioErf9082yMLUG5zFWSZTB3W3kL",
        "lat":location[0], 
        "lon":location[1],
        "fields": ["temp", "precipitation", "wind_gust"],
        "unit_system":"us",  
        } 

        response = requests.get(url, params=payload).json()

     

        climate_data_packet[location[2]] = response["temp"] ["value"]
        
    for city, temp in climate_data_packet.items():

        print(f"The temp is {temp} in {city}.")    
    return climate_data_packet

climate_data = climate(city_list)
#print(climate_data)
 #expects to see real numbers

#TODO construct a list of places that are tuples lat and long
#(lat, long)
# you can use [] to retrieve items by position, like you can in list
# ex. (lat, long)[0] = lat



def get_weather_data(place_list):
  # get lats and longs from tuples
  # give me temp and precip for a location, given lat and long
  # it will make a request to the 'realtime' url that we used below
  pass
