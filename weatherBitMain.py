from typing import Optional

import requests


def get_current_weather(city_current):
    # obtain url with desired city
    url = 'http://localhost:8001/current/' + city_current
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        # print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)


def get_current_weather_lon_lat(lon, lat):
    # obtain url with desired city
    url = 'http://localhost:8001/current/' + lon + "/" + lat
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        # print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)


def get_daily_forecast(city_forecast):
    # obtain url with desired city
    url = 'http://localhost:8001/forecast/daily/' + city_forecast
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        # print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)


def get_daily_forecast_lon_lat(lon, lat):
    # obtain url with desired city
    url = 'http://localhost:8001/forecast/daily/' + lon + "/" + lat
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        # print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)


# if __name__ == '__main__':
#     city = input("Enter the city or zip code you would like to get data from: ")
#     current_weather = get_current_weather(city)

#     daily_weather = get_daily_forecast(city)

#     lon = input("Enter the longitude you would like to get data from: ")
#     lat = input("Enter the latitude you would like to get data from: ")

#     lat_lon_current = get_current_weather_lon_lat(lon, lat)
#     lat_lon_forecast = get_daily_forecast_lon_lat(lon, lat)
