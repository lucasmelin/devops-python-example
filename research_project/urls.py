#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: urls.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Oct 23, 2018
Python version: 3.7

This file provides the url patterns to match inside the research_project app,
and maps each pattern to a view.
"""
from django.urls import path

from . import views

# Prefix when referencing a url in this app
app_name = 'research_project'
# Patterns to match when determining which view to redirect to
urlpatterns = [
    path('', views.index, name='index'),
    path('journal', views.journal, name='journal'),
    path('addentry', views.add_journal_entry, name='add_journal_entry')
]
