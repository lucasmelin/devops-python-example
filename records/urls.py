from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /records/upload
    path('upload', views.upload_csv, name='upload'),
    # ex: /records/10/
    path('<int:commodity_id>/', views.detail, name='detail'),
]
