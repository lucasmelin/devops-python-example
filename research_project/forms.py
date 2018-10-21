#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: forms.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Oct 20, 2018
Python version: 3.7

"""
from django import forms


class GreetingForm(forms.Form):
    """
    The form to display for modifying the greeting. When the form is submitted,
    it will be validated by this function to determine if it meets the restrictions
    """
    new_greeting = forms.CharField(label='New Greeting', max_length=100)
