#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: models.py
Author: Lucas Melin
Date created: Oct 16, 2018
Date last modified: Oct 21, 2018
Python version: 3.7

"""
from django import forms


class UploadFileForm(forms.Form):
    """
    Displays a file name field and a file upload field.
    """
    title = forms.CharField(max_length=50)
    file = forms.FileField()
