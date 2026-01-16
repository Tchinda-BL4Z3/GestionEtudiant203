"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from scheduler import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Routes Admin
    path('admin-console/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-salles/', views.admin_salles, name='admin_salles'),
    path('admin-classes/', views.admin_classes, name='admin_classes'),
    path('admin-ue/', views.admin_ue, name='admin_ue'),

    path('admin-salles/delete/<int:id>/', views.delete_salle, name='delete_salle'),
    path('admin-classes/delete/<int:id>/', views.delete_classe, name='delete_classe'),
    path('admin-ue/delete/<int:id>/', views.delete_ue, name='delete_ue'),
    
    path('delete/<str:model_type>/<int:id>/', views.delete_item, name='delete_item'),
]