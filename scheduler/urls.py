from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('emploi-du-temps/', views.afficher_emploi_temps, name='emploi_temps'),
]