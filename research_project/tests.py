#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: tests.py
Author: Lucas Melin
Date created: Oct 19, 2018
Date last modified: Nov 11, 2018
Python version: 3.7

"""
from django.test import TestCase
from research_project.views import entry_to_date


class JournalTestCase(TestCase):
    def test_sorting_by_date(self):
        """
        Sort a list of 3 dummy journal entries by the creation date.
        """
        unsorted_entries = [['Sunday, October 21, 2018', "A - Entry"], ['Tuesday, May 1, 2018', "B - Entry"],
                            ['Tuesday, September 4, 2018', "C - Entry"]]
        unsorted_entries.sort(key=entry_to_date)
        sorted_entries = [['Tuesday, May 1, 2018', "B - Entry"],
                          ['Tuesday, September 4, 2018', "C - Entry"], ['Sunday, October 21, 2018', "A - Entry"]]
        self.assertEqual(unsorted_entries, sorted_entries)

    def test_sorting_by_date_reverse(self):
        """
        Sort a list of 3 dummy journal entries by the reverse creation date.
        """
        unsorted_entries = [['Sunday, October 21, 2018', "A - Entry"], ['Tuesday, May 1, 2018', "B - Entry"],
                            ['Tuesday, September 4, 2018', "C - Entry"]]
        unsorted_entries.sort(key=entry_to_date, reverse=True)
        sorted_entries = [['Sunday, October 21, 2018', "A - Entry"],
                          ['Tuesday, September 4, 2018', "C - Entry"], ['Tuesday, May 1, 2018', "B - Entry"]]
        self.assertEqual(unsorted_entries, sorted_entries)
