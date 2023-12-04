from json import JSONDecodeError
from typing import Optional

import requests
import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/current/{city_current}')
def current_weather(city_current):
    # print(city_current)
    if city_current.isdigit():
        api_url = f'http://api.weatherbit.io/v2.0/current?key=b22ce9e283d1449e8b14940a35fa9f06&units=I' \
                  f'&postal_code={city_current}'
    else:
        api_url = f'http://api.weatherbit.io/v2.0/current?key=b22ce9e283d1449e8b14940a35fa9f06&units=I' \
                  f'&city={city_current}'
    # print(api_url)
    response = requests.get(api_url)
    print(response)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/current/{lon}/{lat}')
def current_weather(lon: str = "", lat: str = ""):
    api_url = f'http://api.weatherbit.io/v2.0/current?key=b22ce9e283d1449e8b14940a35fa9f06&units=I' \
              f'&lat={lat}' \
              f'&lon={lon}'
    # print(api_url)
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/forecast/daily/{city_forecast}')
def forecast_daily(city_forecast):
    if city_forecast.isdigit():
        api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=b22ce9e283d1449e8b14940a35fa9f06&units=I&days=7&' \
                  f'postal_code={city_forecast}'
    else:
        api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=b22ce9e283d1449e8b14940a35fa9f06&units=I&days=7&' \
                  f'city={city_forecast}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/forecast/daily/{lon}/{lat}')
def forecast_daily(lon: str = "", lat: str = ""):
    api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=b22ce9e283d1449e8b14940a35fa9f06&days=7&units=I' \
              f'&lat={lat}' \
              f'&lon={lon}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
