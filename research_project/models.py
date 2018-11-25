#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: models.py
Author: Lucas Melin
Date created: Nov 24, 2018
Date last modified: Nov 24, 2018
Python version: 3.7

"""
from django.db import models
from django.utils import timezone


class Weather(models.Model):
    """
    Models all the fields for the Weather API response.
    """
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    timestamp = models.DateTimeField()
    city = models.CharField(max_length=30, default="")
    country = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=30, default="")

    def __str__(self):
        """
        String representation of a Weather object.
        Prints the location, timestamp and temperature.
        """
        return '{} {} {} {}'.format(self.city, self.country, self.timestamp, self.temperature)


def save_weather(weather):
    print(weather)
    temperature = weather.get('main').get('temp')
    city = weather.get('name')
    country = weather.get('sys').get('country')
    description = weather.get('weather')[0].get('description')
    timestamp = timezone.now()
    w = Weather(temperature=temperature, city=city, country=country, description=description, timestamp=timestamp)
    w.save()
