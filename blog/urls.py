from django.urls import path
from . import views

urlpatterns = [
    path('', views.grafica, name='grafica'),
]