#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: recordfilters.py
Author: Lucas Melin
Date created: Oct 19, 2018
Date last modified: Oct 20, 2018
Python version: 3.7

This file contains filters, which are pieces of code that run against
built-in or user created Django templates in order to modify their contents.
These filters are used in the research_project app.
"""
from django import template

register = template.Library()


@register.filter(name='addCssClass')
def add_css_class(value, arg):
    """
    Adds the contents of the arg parameter as
    css class attributes to the current form
    field.
    :param value: the form field to modify
    :param arg: string containing one or more css classes to add, separated by a space
    :return: the form field with the css classes applied
    """
    return value.as_widget(attrs={'class': arg})
