"""djangomap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from datetime import datetime
from django.urls import path

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from obsnet import  views
from obsnet import updatebd
from django.views.generic import TemplateView
from django.conf.urls import  re_path
from djgeojson.views import GeoJSONLayerView
from obsnet.models import WeatherStation
from obsnet.models import Country
from obsnet.models import Adt
from obsnet.models import Fed_o
from obsnet.models import Subrf
from obsnet.models import Ugms
from obsnet.models import Oblasti
from djgeojson.views import TiledGeoJSONLayerView
from obsnet.views import StationGeoJSONLayerView
from obsnet.views import SubrfGeoJSONLayerView
from obsnet.views import FedoGeoJSONLayerView
from obsnet.updatebd import DatabaseView

app_name = "obsnet"
urlpatterns = [
    path('', views.home, name='home'),
    
    re_path(r'^database_update', updatebd.DatabaseView, name = 'bd'),
    #re_path(r'^update', updatebd.create_country, name = 'updatebase'),
    
    re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    re_path(r'^stations.geojson$', GeoJSONLayerView.as_view(model=WeatherStation, properties=['name_station_rus', 'station_index']), name='stations'),    
    re_path(r'^adt.geojson$', GeoJSONLayerView.as_view(model=Adt), name='adt'),
    
    #re_path(r'^filterstation.geojson/(?P<id_ugms>\d{2})$', StationGeoJSONLayerView.as_view(), name = 'filterstation'),
    re_path(r'^filterstation.geojson/(\d+)$', views.StationGeoJSONLayerView.as_view(), name = 'filterstation'),
    
    re_path(r'^ugms.geojson$', GeoJSONLayerView.as_view(), name='ugms'),
    re_path(r'^oblasti.geojson$', GeoJSONLayerView.as_view(model=Oblasti), name='oblasti'),
    
    re_path(r'^subrf.geojson/(\d+)$', SubrfGeoJSONLayerView.as_view(), name='subrf'),
   
    re_path(r'^fedo.geojson/(\d+)$', FedoGeoJSONLayerView.as_view(), name='fedo'),
    re_path(r'^country.geojson/(\d+)$', GeoJSONLayerView.as_view(model=Country, geometry_field = 'country_border'), name='country')
]
