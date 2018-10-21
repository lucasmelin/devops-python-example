#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: views.py
Author: Lucas Melin
Date created: Oct 19, 2018
Date last modified: Oct 20, 2018
Python version: 3.7
"""
from django.shortcuts import render
from .forms import GreetingForm


def index(request):
    """
    This view is called when the research_project index is accessed.
    If the request was a POST, we attempt to modify the greeting text
    file. If the request was a GET, we display the greeting from the
    text file.
    """
    # Default greeting
    greeting = "Welcome"
    # Lucas Melin
    if request.method == 'POST':
        # Verify the contents of the POST
        form = GreetingForm(request.POST)
        if form.is_valid():
            # Write the new greeting to file
            greeting = form.cleaned_data['new_greeting']
            # Open file for writing
            try:
                with open("greeting.txt", "w") as greet:
                    greet.write(greeting)
            except IOError:
                # Could not access file. Ignore the exception,
                # since the greeting already has a default value
                pass
    else:
        # Request was not a POST, display greeting stored in file
        form = GreetingForm()
        # Read the greeting from file
        try:
            with open("greeting.txt") as greet:
                greeting = greet.read()
        except IOError:
            # Could not access file. Ignore the exception,
            # since the greeting already has a default value
            pass
    # Save the greeting and form as a dictionary to return
    # with the request
    context = {'greeting': greeting, 'form': form}
    return render(request, 'research_project/index.html', context)
