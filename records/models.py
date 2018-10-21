#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: models.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Oct 21, 2018
Python version: 3.7

This models a Commodity as defined in the original dataset found here:
Statistics Canada. (May 30, 2018). Food available in Canada [web[age] Retrieved on October 13, 2018
from  https://open.canada.ca/data/en/dataset/a683c640-b5fd-48f8-a0f1-d619b8f7e04c
Used under the Open Government Licence found at
https://open.canada.ca/en/open-government-licence-canada
"""
from django.db import models
from django.urls import reverse
import csv
from io import StringIO


class Commodity(models.Model):
    """
    Models all the fields for a Commodity, and defines the preset
    choices, default choice, and max length where applicable.
    """
    KILOGRAMS = "KGPY"
    LITRES = "LPY"
    UNIT_OF_MEASUREMENT_CHOICES = (
        (KILOGRAMS, "Kilograms per person, per year"),
        (LITRES, "Litres per person, per year")
    )
    UNITS = "U"
    THOUSANDS = "K"
    SCALAR_FACTOR_CHOICES = (
        (UNITS, "Units"),
        (THOUSANDS, "Thousands")
    )
    FOODAVAILABLE = "FA"
    FOODADJUSTEDFORLOSS = "FAFL"
    FOOD_CATEGORY_CHOICES = (
        (FOODAVAILABLE, "Food available"),
        (FOODADJUSTEDFORLOSS, "Food available, adjusted for loss")
    )
    unit_of_measurement = models.CharField(
        max_length=4,
        choices=UNIT_OF_MEASUREMENT_CHOICES,
        default=KILOGRAMS,
    )
    scalar_factor = models.CharField(
        max_length=1,
        choices=SCALAR_FACTOR_CHOICES,
        default=UNITS,
    )
    food_category = models.CharField(
        max_length=4,
        choices=FOOD_CATEGORY_CHOICES,
        default=FOODAVAILABLE,
    )
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """
        String representation of a Commodity object.
        Prints the name, value and unit of measurement
        """
        return '{} {} {}'.format(self.name, self.value, self.unit_of_measurement)

    def get_absolute_url(self):
        """
        Gets called after the edit occurs in order to redirect to
        the proper details page.
        """
        return reverse('records:commodity-detail', kwargs={'commodity_id': self.pk})


def save_csv(csv_file):
    """
    Analyses the Commodity csv file and creates new Commodity
    database records.
    """
    # Parse the inMemory file as strings instead of bytes
    csvf = StringIO(csv_file.read().decode())

    csv_reader = csv.DictReader(csvf)
    for row in csv_reader:
        # Account for empty cell values in the value column
        row_value = row['VALUE']
        if not row_value:
            row_value = 0.0
        # Create each row
        c, created = Commodity.objects.get_or_create(
            food_category=row['Food categories'],
            name=row['Commodity'],
            unit_of_measurement=row['UOM'],
            scalar_factor=row['SCALAR_FACTOR'],
            value=row_value,
        )
        # Save each row
        c.save()
