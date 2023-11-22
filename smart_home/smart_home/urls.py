"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from measurement.views import SListAPIView, MListAPIView
from measurement.views import SensorView, MCreateViewSet, SCreateViewSet
from rest_framework.routers import DefaultRouter

m = DefaultRouter()
m.register('MCreate', MCreateViewSet)
s = DefaultRouter()
s.register('SCreate', SCreateViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', SListAPIView.as_view()),
    path('sensor/<pk>', SensorView.as_view()),
    path('mlist/', MListAPIView.as_view()),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
] + m.urls + s.urls
