#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: models.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Nov 11, 2018
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
    Lucas Melin
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
    UNIT_OF_MEASUREMENT_ID_CHOICES = (
        ("194", "194"),
        ("205", "205")
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
    ref_date = models.IntegerField(default=1900)
    geo = models.CharField(max_length=20, default="")
    dguid = models.CharField(max_length=20, default="")
    unit_of_measurement_id = models.IntegerField(
        choices=UNIT_OF_MEASUREMENT_ID_CHOICES,
        default="194"
    )
    scalar_id = models.IntegerField(
        choices=((0, 0), (3, 3)),
        default=0
    )
    vector = models.CharField(max_length=10, default="")
    coordinate = models.CharField(max_length=10, default="")
    status = models.CharField(max_length=10, default="")
    terminated = models.BooleanField(default=False)

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
    csvf = StringIO(csv_file.read().decode('utf-8-sig'))

    csv_reader = csv.DictReader(csvf)
    rows_to_add = []
    for row in csv_reader:
        # Account for empty cell values in the value column
        row_value = row['VALUE']
        if not row_value:
            row_value = 0.0

        # Create each entry
        c = Commodity(
            ref_date=row['REF_DATE'],
            geo=row['GEO'],
            dguid=row['DGUID'],
            food_category=row['Food categories'],
            name=row['Commodity'],
            unit_of_measurement=row['UOM'],
            unit_of_measurement_id=row['UOM_ID'],
            scalar_factor=row['SCALAR_FACTOR'],
            scalar_id=row['SCALAR_ID'],
            vector=row['VECTOR'],
            coordinate=row['COORDINATE'],
            status=row['STATUS'],
            value=row_value,
            terminated=(row['TERMINATED'] == 't')
        )
        # Add to list of entries to insert
        rows_to_add.append(c)
    # Bulk create all the rows at the same time
    Commodity.objects.bulk_create(rows_to_add)

