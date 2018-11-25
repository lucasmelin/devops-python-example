#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: tasks.py
Author: Lucas Melin
Date created: Nov 5, 2018
Date last modified: Nov 9, 2018
Python version: 3.7

This file is read when run_huey executes in order to parse which functions
are multi-threaded.
"""
from huey.contrib.djhuey import task
from .charts import CommodityBarChart, CommodityLineGraph, get_data_food_available_2017


@task()
def create_chart():
    """
    Asynchronously generate a bar chart containing the food available in 2017.
    """
    chart_commodity = CommodityBarChart(
        height=600,
        width=800,
        explicit_size=True
    )
    chart_commodity.generate('commodity_2017.svg', get_data_food_available_2017)


@task()
def create_historical_chart(commodity_id):
    """
    Asynchronously generate a line containing the historical value of a specific commodity.
    """
    chart_commodity = CommodityLineGraph(
        height=600,
        explicit_size=True
    )
    chart_name = str(commodity_id) + '.svg'
    chart_commodity.generate(chart_name, CommodityLineGraph.get_data_historical_commodity, commodity_id)
