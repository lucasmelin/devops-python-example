#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: tests.py
Author: Lucas Melin
Date created: Oct 19, 2018
Date last modified: Oct 21, 2018
Python version: 3.7

"""
from decimal import Decimal

from django.test import TestCase
from records.models import Commodity


class CommodityTestCase(TestCase):
    def setUp(self):
        """
        Add a Commodity record for use by the tests.
        """
        Commodity.objects.create(name="Purple Avocadoes", value=0.2)

    def test_commodity_exists(self):
        """
        Verify that the commodity created in the setUp exists with the correct value.
        """
        avocado = Commodity.objects.get(name="Purple Avocadoes")
        self.assertEqual(avocado.value, Decimal("0.2"))

    def test_commodity_does_not_exist(self):
        """
        Verify that a non-existent commodity raises a DoesNotExist error.
        """
        self.assertRaises(Commodity.DoesNotExist, Commodity.objects.get, name="Does not exist")

    def test_update_commodity_value(self):
        """
        Verify that we can update the value of a Commodity.
        """
        avocado = Commodity.objects.get(name="Purple Avocadoes")
        avocado.value = 1.0
        avocado.save()
        new_avocado = Commodity.objects.get(name="Purple Avocadoes")
        self.assertEqual(new_avocado.value, Decimal("1.0"))

    def test_delete_commodity(self):
        """
        Verify that we can delete a Commodity.
        """
        avocado = Commodity.objects.get(name="Purple Avocadoes")
        avocado.delete()
        self.assertRaises(Commodity.DoesNotExist, Commodity.objects.get, name="Purple Avocadoes")
