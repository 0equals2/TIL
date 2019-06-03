from django.contrib import admin
from django.urls import path, include
from . import views as master_views # 같은 위치
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', views.index),
    #path('hello/<str:name>/', views.hello)
    path('', include('home.urls')),
]
