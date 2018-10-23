from django.urls import path

from records.views import CommodityCreate, CommodityUpdate, CommodityDelete
from . import views

app_name = 'records'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_csv, name='commodity-upload'),
    path('<int:commodity_id>/view/', views.detail, name='commodity-detail'),
    path('add/', CommodityCreate.as_view(), name='commodity-add'),
    path('<int:pk>/edit/', CommodityUpdate.as_view(), name='commodity-update'),
    path('<int:pk>/delete/', CommodityDelete.as_view(), name='commodity-delete'),
]
