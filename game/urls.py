from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('camp', views.camp),
    path('search', views.search),
    path('restart', views.restart),
]