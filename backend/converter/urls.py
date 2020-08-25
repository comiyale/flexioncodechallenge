from django.urls import path
from . import views

urlpatterns = [
    path('unit/', views.CreateListUnit.as_view(), name=views.CreateListUnit.name),
    path('unit/<int:pk>/', views.DetailUnit.as_view(), name=views.DetailUnit.name),

    path('unittype/', views.CreateListUnitType.as_view(), name=views.CreateListUnitType.name),
    path('unittype/<int:pk>/', views.DetailUnitType.as_view(), name=views.DetailUnitType.name),

    path('convert/', views.ConverterView.as_view(), name=views.ConverterView.name)
   
]