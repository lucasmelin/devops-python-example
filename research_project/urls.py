from django.urls import path

from . import views

app_name = 'research_project'
urlpatterns = [
    path('', views.index, name='index')
]
