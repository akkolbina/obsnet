from django.contrib.gis.geos import Point, Polygon

from obsnet.models import WeatherStation
from obsnet.models import Adt
from obsnet.models import Country
from obsnet.models import Fed_o
from obsnet.models import Subrf

from obsnet.forms import FilterForm
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
import json
import pandas as pd
from obsnet.updatebd import fill_bd
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from djgeojson.serializers import Serializer as GeoJSONSerializer

from djgeojson.views import GeoJSONLayerView
from django.conf.urls import  re_path
from djgeojson.http import HttpGeoJSONResponse
from django.http import HttpResponseRedirect
from django.urls import  reverse


 #class Choice()


def home(request):
    """Renders the home page."""
    #fill_bd()
    assert isinstance(request, HttpRequest)
    id_s = 0
    id_fed = 0
    id_country = 0
    id_ugms_c = 0
    
    if request.method == 'POST':
        #print(getResForm(request))
    # create a form instance and populate it with data from the request:
        form = FilterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #valid = 1
            # process the data in form.cleaned_data as required
            id_s = form.cleaned_data.get('filter_subrf')
            #print(type(id_s))
            #print('ID_S='+id_s)
            if (id_s == '0') : 
                id_s = 0
                #print('ID_S='+id_s)
            id_fed = form.cleaned_data.get('filter_fedo')
            if (id_fed == '0') : 
                id_fed = 0
                #print('2'+id_fed)
            id_country = form.cleaned_data.get('filter_country')
            if (id_country == '0') : 
                id_country = 0
                
            id_ugms_c = form.cleaned_data.get('filter_ugms')
            if (id_ugms_c == '0') : 
                id_ugms_c = 0
            #print('view!'+id_ugms_c)
            #stations = WeatherStation.objects.filter(id_ugms = idugms_new)
            #inf = 
            #newst = WeatherStation.objects.filter(id_subrf = int(id_s))
            #newstat = list()
            #for obw in newst:
            #    newstat.append({
            #   'station_index': obw.station_index,
            #   'name_station_rus': obw.name_station_rus,
            #   'geom': obw.geom
            #   })
                #print(obw.station_index)
            #ser = serialize('geojson', newstat)
            #ser = GeoJSONSerializer().serialize(newstat)
            #print(ser)
            #filterstation = GeoJSONLayerView.as_view(model=newst)
            #print(str(id_subrf) +" = ID ")
            #print(filterstation)
            # redirect to a new URL:
            httpres = StationGeoJSONLayerView()
            
            #print(httpres.ppp)
            #print(type(httpres))
            #print(dir(httpres))
            #answer = HttpResponseRedirect(reverse('filterstation'))
            #print(answer)
            #geojson_data = WeatherStation.objects.filter(id_ugms = id_ugms_c)
            #geojson = serialize('geojson', geojson_data, geometry_field='geom', with_modelname=False)

            #ser = GeoJSONSerializer().serialize(WeatherStation.objects.filter(id_ugms = id_ugms_c), use_natural_keys=True, with_modelname=False)
            #print(ser)
            return render(
                request,
                'obsnet/index.html',
               
                { 
                    'form' : form,
                    'title' : 'Home Page',
                    'year' : datetime.now().year,
                    #'valid' : valid,
                    'id_s' : id_s,
                    'id_fed' : id_fed,
                    'id_country' : id_country,
                    'id_ugms' : id_ugms_c, 
                    #'filterstation' : filterstation,
                    #'newstat':  newstat,
                   # 'subrf' : subrf,
                },        
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilterForm()
   
    
    return render(
        request,
        'obsnet/index.html',
        {
            'form' : form,
            'title' : 'Home Page',
            'year' : datetime.now().year,
                                'id_s' : id_s,
                    'id_fed' : id_fed,
                    'id_country' : id_country,
                    'id_ugms' : 0, 
            #'subrf_new' : ser,
            #'subrf' : subrf,
        },        
    )



def newview():
    httpres = StationGeoJSONLayerView()
    #print(httpres)

def getResForm(request):
    id_ugms_c = None
    assert isinstance(request, HttpRequest)
    form = FilterForm(request.POST)
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            id_ugms_c = form.cleaned_data.get('filter_ugms')
            if (id_ugms_c == '0') : 
                id_ugms_c = None
    return id_ugms_c


def getspisok():
    #assert isinstance(request, HttpRequest)
    #print(getResForm(request))
    #k = getResForm(request)
    #if request
    spisok = WeatherStation.objects.filter(id_ugms = 3)
    return spisok



class StationGeoJSONLayerView(GeoJSONLayerView):
    
    ugmsid = 3

    def ppp(self):
        idu = self.kwargs.get('filter_ugms')
        return idu
        
    
    #idu = ppp()
    #print("filter")
    #queryset = getspisok()
    model = WeatherStation
    properties = ['name_station_rus', 'station_index', 'id_subrf', 'id_country',  'id_ugms' ]
    #filter_choice = 1

    
    def get_queryset(self):
        #print(self.request)
        suburl = str(self.request)
        #print('STROCHKA' +  str(len(suburl)))
        s_suburl = suburl.split('/')
        idugms_new = s_suburl[2].replace('\'>', '')
        #print(idugms_new)
        #print(getResForm(self.request))
        filterUgms = None
        #filter_val = self.request.POST.get('filter_ugms')
        assert isinstance(self.request, HttpRequest)
        
        if self.request.method == 'POST':
            form = FilterForm(self.request.POST)
            if form.is_valid():
                filterUgms = form.cleaned_data.get('filter_ugms')
                #print(form.cleaned_data.get('filter_ugms'))
                if (filterUgms == '0') : 
                    filterUgms = None
        #else:
            #form1 = FilterForm(self.request.GET)
            #print(self.request.GET.get('ugms'))
        #print(self.request)
        if (idugms_new != '0'):
            spisok = WeatherStation.objects.filter(id_ugms = idugms_new)
            #print ("Filtered by UGMS")
        else:
            spisok = WeatherStation.objects.all()
            #print ("Filtered by COUNTRY")
        return spisok    
  
  
    def head(self, *args, **kwargs):
        #choice_stations = WeatherStation.get_queryset().filter(id_subrf_id = 2)
        response = HttpGeoJSONResponse('')
        # RFC 1123 date format
        #response['filterstation'] = choice_stations
        return response

class SubrfGeoJSONLayerView(GeoJSONLayerView):
    model = Subrf
    properties = ['id_subrf', 'name_subrf']
    geometry_field = 'subrf_border'
    def head(self, *args, **kwargs):
        response = HttpGeoJSONResponse('')
        return response
        
class FedoGeoJSONLayerView(GeoJSONLayerView):
    model=Fed_o 
    properties=['id_fed_o', 'name_fed_o'] 
    geometry_field = 'fed_o_border'
    def head(self, *args, **kwargs):
        response = HttpGeoJSONResponse('')
        return response

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'obsnet/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'obsnet/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


