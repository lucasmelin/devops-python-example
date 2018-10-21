#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: views.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Oct 20, 2018
Python version: 3.7
"""
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import UploadFileForm
from .models import save_csv, Commodity


def index(request):
    """
    Function that gets called when the records index is visited. Returns the
    10 most recently added Commodities.
    :param request:
    :return:
    """
    # Sort the commodities in descending id order, and return a
    # slice of the last 10 items.
    latest_commodity_list = Commodity.objects.order_by('-id')[:10]
    context = {'latest_commodity_list': latest_commodity_list}
    return render(request, 'records/index.html', context)


def upload_csv(request):
    """
    If the request is a POST, validate and upload the csv data.
    Otherwise, return the form to allow the user to upload a csv.
    """
    if request.method == 'POST':
        # Long running if the csv file is large
        save_csv(request.FILES['recordfile'])
        return HttpResponseRedirect('/records')
    else:
        # Return the upload form
        form = UploadFileForm()
    return render(request, 'records/upload.html', {'form': form})


def detail(request, commodity_id):
    """
    Return the details of the commodity specified by the id.
    """
    # Try to retrieve the appropriate item from the database
    try:
        commodity = Commodity.objects.get(pk=commodity_id)
    except Commodity.DoesNotExist:
        raise Http404("Commodity does not exist")
    return render(request, 'records/commodity_detail.html', {'commodity': commodity})


class CommodityCreate(CreateView):
    model = Commodity
    fields = ['name', 'food_category', 'value', 'unit_of_measurement', 'scalar_factor']


class CommodityUpdate(UpdateView):
    model = Commodity
    fields = ['name', 'food_category', 'value', 'unit_of_measurement', 'scalar_factor']


class CommodityDelete(DeleteView):
    model = Commodity
    success_url = reverse_lazy('records:index')
