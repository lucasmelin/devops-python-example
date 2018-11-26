#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File name: views.py
Author: Lucas Melin
Date created: Oct 15, 2018
Date last modified: Nov 11, 2018
Python version: 3.7
"""
from django.contrib.staticfiles import finders
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import UploadFileForm
from .models import save_csv, Commodity
from .tasks import create_chart, create_historical_chart


def index(request):
    """
    Function that gets called when the records index is visited. Returns the
    current page of Commodities.
    """
    # Sort the commodities in descending id order
    commodity_list = Commodity.objects.all().order_by('-id')
    # Show 5 commodities per page
    paginator = Paginator(commodity_list, 5)
    # Get the page number from the query param
    page = request.GET.get('page')
    # Create a list of commodities from the current page's results
    latest_commodity_list = paginator.get_page(page)
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


def commodity_chart(request):
    """
    Generate a chart containing all commodity data from 2017.
    """
    create_chart()
    context = {'chart_svg': 'charts/commodity_2017.svg'}
    return render(request, 'records/chart.html', context)


def historical_data(request, commodity_id):
    """
    Generate a chart containing all historical values for the given commodity.
    """
    chart_to_render = 'charts/' + str(commodity_id) + '.svg'
    if finders.find(chart_to_render):
        context = {'chart_svg': chart_to_render}
        return render(request, 'records/chart.html', context)
    create_historical_chart(commodity_id)
    return render(request, 'records/chart_loading.html')


class CommodityCreate(CreateView):
    """
    Renders a view to create a new Commodity with the specified fields.
    """
    model = Commodity
    fields = ['ref_date', 'geo', 'dguid', 'food_category', 'name', 'value', 'unit_of_measurement', 'scalar_factor',
              'vector', 'coordinate', 'status', 'symbol', 'decimals', 'terminated']


class CommodityUpdate(UpdateView):
    """
    Renders a view to modify and existing Commodity with the specified fields.
    """
    model = Commodity
    fields = ['ref_date', 'geo', 'dguid', 'food_category', 'name', 'value', 'unit_of_measurement', 'scalar_factor',
              'vector', 'coordinate', 'status', 'symbol', 'decimals', 'terminated']


class CommodityDelete(DeleteView):
    """
     Renders a view to delete a Commodity. Redirects to 'records:index' when deletion is complete.
    """
    model = Commodity
    success_url = reverse_lazy('records:index')
