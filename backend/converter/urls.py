from django.urls import path
from . import views

urlpatterns = [
    path('get_units/', views.list_units),
    path('convert/', views.ConverterView.as_view(), name=views.ConverterView.name)
]