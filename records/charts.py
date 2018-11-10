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


def get_data_food_available_2017():
    data = {}
    for commodity in Commodity.objects.all().filter(ref_date='2017').filter(
            unit_of_measurement__exact="Kilograms per person, per year").filter(
            food_category__exact='Food available').order_by('-value')[:20]:
        print(commodity)
        # Multiply the value if necessary
        if commodity.scalar_factor is "thousands":
            data[commodity.name] = commodity.value * 1000
        data[commodity.name] = commodity.value
    return data




class CommodityBarChart:

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Commodities'

    def generate(self, filename, get_data, *args, **kwargs):
        """
        This method will call the passed in function `get_data` to
        generate the required data for this particular chart.
        """
        # Get the chart data
        chart_data = get_data(*args, **kwargs)

        # Add the data to the chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Save the generated chart to the static directory
        return self.chart.render_to_file('records/static/charts/' + filename)


class CommodityLineGraph:

    def __init__(self, **kwargs):
        self.chart = pygal.Line(**kwargs)
        self.chart.title = 'Commodities'

    def generate(self, filename, get_data, *args, **kwargs):
        """
        This method will call the passed in function `get_data` to
        generate the required data for this particular chart.
        """
        # Get the chart data
        chart_data = get_data(self, *args, **kwargs)

        # Add the data to the chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Save the generated chart to the static directory
        return self.chart.render_to_file('records/static/charts/' + filename)

    def get_data_historical_commodity(self, commodity_id):
        data = {}
        reference = Commodity.objects.get(pk=commodity_id)
        for commodity in Commodity.objects.all().filter(name__exact=reference.name):
            data.setdefault(commodity.food_category, []).append(commodity.value)
        return data

