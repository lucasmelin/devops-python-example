#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: charts.py
Author: Lucas Melin
Date created: Nov 1, 2018
Date last modified: Nov 9, 2018
Python version: 3.7

"""
import pygal

from .models import Commodity


class CommodityLineGraph():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Commodities'

    def get_data(self):
        data = {}
        for commodity in Commodity.objects.all():
            data[commodity.name] = commodity.value
        return data

    def generate(self):
        # Get the chart data
        chart_data = self.get_data()

        # Add the data to the chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered chart
        return self.chart.render(is_unicode=True)