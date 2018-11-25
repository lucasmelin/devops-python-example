#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: views.py
Author: Lucas Melin
Date created: Oct 19, 2018
Date last modified: Nov 24, 2018
Python version: 3.7
"""
import datetime
import os

from django.shortcuts import render, redirect

from research_project.models import Weather
from .forms import GreetingForm, JournalEntryForm


def index(request):
    """
    This view is called when the research_project index is accessed.
    If the request was a POST, we attempt to modify the greeting text
    file. If the request was a GET, we display the greeting from the
    text file.
    """
    # Default greeting
    greeting = "Welcome"
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
    # Get the most recent weather data from the database
    try:
        latest_weather = Weather.objects.latest('timestamp')
    except Weather.DoesNotExist:
        # We have no weather data in the database yet
        latest_weather = None
    # Save the greeting, weather and form as a dictionary to return
    # with the request
    context = {'greeting': greeting, 'greet_form': form, 'weather': latest_weather}
    return render(request, 'research_project/index.html', context)


def journal(request):
    """
    This view is called when the research_project journal page is accessed.
    """
    # Save the greeting and forms as a dictionary to return
    # with the request
    journal_form = JournalEntryForm()
    journal_data = get_journal_entries("journal.txt")

    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        # Sort the entries by date descending
        journal_data.sort(key=entry_to_date, reverse=False)
        sort_order = 'asc'
    elif sort_order == 'asc':
        # Sort the entries by date ascending
        journal_data.sort(key=entry_to_date, reverse=True)
        sort_order = 'desc'
    context = {'journal_form': journal_form, 'journal_data': journal_data, 'sort_order': sort_order}
    return render(request, 'research_project/journal_entries.html', context)


def entry_to_date(to_sort):
    """
    Returns the first item of the list parsed as a date.
    """
    return datetime.datetime.now().strptime(to_sort[0], "%A, %B %d, %Y")


def add_journal_entry(request):
    """
        This view is called when the journal entry form is submitted.
        If the request was a POST, we add an entry to the journal.
        """
    if request.method == 'POST':
        # Verify the contents of the POST
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            # Write the new entry to file
            entry = form.cleaned_data['new_journal_entry']
            # Open file for appending
            try:
                with open("journal.txt", "a") as j:
                    j.write(datetime.datetime.now().strftime("%A, %B %d, %Y") + '\t')
                    j.write(entry + '\n')
            except IOError:
                # Could not access file. Ignore the exception,
                # since the greeting already has a default value
                pass
    return redirect('research_project:journal')


def get_journal_entries(filename):
    """
    Retrieve all the journal entries from the file and return them as a list.
    """
    entries = []

    if os.path.exists(filename):
        with open(filename) as j:
            for entry in j.readlines():
                entry_list = [piece.strip() for piece in entry.split('\t')]
                entries.append(entry_list)
    return entries
