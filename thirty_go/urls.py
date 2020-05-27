from django.urls import path
from . import views

app_name = 'thirty_go'
urlpatterns = [
    path('', views.index, name='index'),
]
