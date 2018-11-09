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
from .charts import CommodityLineGraph


@task()
def create_chart():
    chart_commodity = CommodityLineGraph(
        height=600,
        width=800
    )
    chart_commodity.generate('commodity_async.svg')
