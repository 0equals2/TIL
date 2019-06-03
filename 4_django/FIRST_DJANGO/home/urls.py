from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('contact/', views.contact),
    path('help_me/', views.help_me),
]