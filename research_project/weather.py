#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: weather.py
Author: Lucas Melin
Date created: Nov 22, 2018
Date last modified: Nov 22, 2018
Python version: 3.7

"""
import requests


def get_current_ottawa_weather():
    """
    Makes an HTTP request to the OpenWeatherMap API and
    returns the parsed JSON response as a dictionary.
    """
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    app_id = '0b6b8419f95b4f441e51b77ad2445f40'
    request_parameters = {'q': 'Ottawa', 'appid': app_id, 'units': 'metric'}
    response = requests.get(url=api_url, params=request_parameters)
    return response.json()
