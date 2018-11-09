#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: urls.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Oct 23, 2018
Python version: 3.7

This file provides the url patterns to match inside the records app,
and maps each pattern to a view.
"""
from django.urls import path

from records.views import CommodityCreate, CommodityUpdate, CommodityDelete
from . import views

app_name = 'records'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_csv, name='commodity-upload'),
    path('chart/', views.commoditychart, name='commodity-chart'),
    path('<int:commodity_id>/view/', views.detail, name='commodity-detail'),
    path('add/', CommodityCreate.as_view(), name='commodity-add'),
    path('<int:pk>/edit/', CommodityUpdate.as_view(), name='commodity-update'),
    path('<int:pk>/delete/', CommodityDelete.as_view(), name='commodity-delete'),
]
