from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear/', views.crear),
    path('crear/<dni>/', views.crear),
    path('crear/<dni>/<nombre>/', views.crear),
    path('crear/<dni>/<nombre>/<apellido>/', views.crear),
    path('mostrar/', views.mostrar),
]