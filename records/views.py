from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import save_csv, Commodity
from .forms import UploadFileForm


def index(request):
    with open("greeting.txt") as greet:
        greeting = greet.read()
    latest_commodity_list = Commodity.objects.order_by('-id')[:10]
    context = {'greeting': greeting, 'latest_commodity_list': latest_commodity_list}
    return render(request, 'records/index.html', context)


def upload_csv(request):
    if request.method == 'POST':
        # Long running if the csv file is large
        save_csv(request.FILES['recordfile'])
        return HttpResponseRedirect('/records')
    else:
        form = UploadFileForm()
    return render(request, 'records/upload.html', {'form': form})


def detail(request, commodity_id):
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
