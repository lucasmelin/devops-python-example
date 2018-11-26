#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: tasks.py
Author: Lucas Melin
Date created: Nov 24, 2018
Date last modified: Nov 25, 2018
Python version: 3.7

This file is read when run_huey executes in order to parse which functions
are multi-threaded.
"""
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from .weather import get_current_ottawa_weather
from .models import Weather, save_weather
from django.utils import timezone
import datetime


@db_periodic_task(crontab(minute='*/5'))
def get_current_weather():
    """
    Retrieve the current weather information and store it in the database.
    """
    try:
        latest_weather = Weather.objects.latest('timestamp')
        updated_this_hour = latest_weather.timestamp >= timezone.now() - datetime.timedelta(minutes=5)
        if not updated_this_hour:
            # Last time we got weather data was more than 5 minutes ago
            # so query the weather API and save the data
            current_weather = get_current_ottawa_weather()
            save_weather(current_weather)
    except Weather.DoesNotExist:
        # We have no weather data in the database, so query the API
        # and save the data in the database
        current_weather = get_current_ottawa_weather()
        save_weather(current_weather)
