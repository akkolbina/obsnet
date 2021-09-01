# -*- coding: utf-8 -*-
#from django.contrib.gis.geos import Point, Polygon

from obsnet.models import WeatherStation
from obsnet.models import Adt
from obsnet.models import Country
from obsnet.models import Fed_o
from obsnet.models import Subrf
from obsnet.models import Ugms
from obsnet.models import ClimatData
from obsnet.models import Oblasti


from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
import json
import pandas as pd
from django.contrib.gis.geos import WKTReader
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon 
from django.contrib.gis.geos.collections import MultiPolygon
from django.contrib.gis.geos.collections import GeometryCollection
from django.contrib.gis.geos import GEOSGeometry

#def fill_bd_country():
def fill_bd():
    russia = create_country()
    #russia.save()
    fill_fedo(russia)
    fill_subrf(russia)
    cat_ugms = create_ugms()
    
    #fill_oblasti()
    
    station = create_station_cat(cat_ugms)
    #fill_adt()
    #create_ugms()
    #fill_climatdata()
    print('success!')
    

def DatabaseView(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        #create_country()
        fill_bd()
    return render(
        request,
        'obsnet/database_update.html',
        {
            'title':'Заполнение БД',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def create_station_cat(cat_ugms):
    df = pd.read_csv(r'storage/catalog.csv', sep =';')
    df.info()
    k = len(df.loc[0])
    col = df.columns
    #print(df.loc[0])
    print(df.loc[0, 'Синоптический индекс станции'])
    #цикл для заполения БД, один раз заполнить и закомментить. Пока не доработан.
    id_ugms = 0
    #print(df.shape)
    #for i in range (0, df.shape[0]): 
    for i in range (0, df.shape[0]): 
        id_station = df.loc[i, 'serialNum']
        if pd.isna(df.loc[i, 'Синоптический индекс станции']): 
            station_index = 0
        else:
            station_index = df.loc[i, 'Синоптический индекс станции']
        name_station_rus = df.loc[i, 'StationName']
        name_station_en = ''
        
        for k in range(0, len(cat_ugms)):
            if df.loc[i, 'Название УГМС'] == cat_ugms[k]:
                id_ugms = k+1
            #else: 
            #    id_ugms = 
        id_country = 1
        id_subrf = 1
        latitude = df.loc[i, 'Широта']
        longitude = df.loc[i, 'Долгота']
        geom = Point( longitude, latitude)
        height_above_sea = ''
        access_level = ''
        #geom = Point( fromstr('long'), fromstr('lat'))
        WeatherStation(id_station, station_index, name_station_rus, name_station_en, id_ugms, id_country, id_subrf, latitude, longitude, geom, height_above_sea, access_level).save()
        #station = WeatherStation.objects.create(id_station = id_station, station_index = station_index, name_station_rus = name_station_rus, name_station_en = name_station_en,  latitude = latitude, longitude = longitude, geom = geom , height_above_sea = height_above_sea, access_level = access_level)
        #return station
   
def create_country():
    #assert isinstance(request, HttpRequest)
    #if request.method == "GET":
    #if request.POST.get('click', False):
    
    #очищаем таблицу перед обновлением данных
    Country.objects.all().delete() 
    
    #получаем координаты границы России
    data = ''
    with open(r'storage/admin_level_2.geojson') as project_file:    
        data = json.load(project_file)  

    df = pd.json_normalize(data)
    #df.info()
    features_df = df.loc[0, 'features']
    features = pd.DataFrame(data = features_df)
    #features.info()
    size_feat = features.size
    #print(size_feat)
    #print(features.shape)
    #for i in range (0, size_feat):
    coord = features.loc[0, 'geometry']
    coordinates = pd.DataFrame(data = coord)
    pnt = GEOSGeometry(str(coord))
    
    df2 = pd.read_csv(r'storage/oksm.csv', sep =';')
    df2.info()
    k = len(df2.loc[0])
    colum = df2.columns
    #print(df2.shape[0])
    #id_c = ''
    #for i in range (0, 3): 
    #print(df2.loc[0,'Short Name'])
    con_border = ''
    for i in range (0, df2.shape[0]): 
        id_c = df2.loc[i,'Number']
        #print(i)
        name_c = df2.loc[i,'Short Name']
        #вставляем границы для России
        if (id_c == 185):
            con_border = pnt
        else: 
            con_border = MultiPolygon()
        #print(con_border)
        Country(id_c, name_c, con_border).save()
        
    #print(name_c)
    #df = pd.read_csv(r'storage/admin_level_2.csv', sep =';')
    #df = pd.read_json(r'storage/admin_level_2.geojson')
    #df.info()
    #col = df.columns
   # size_df = df.size
   # print(size_df)
   # for i in range (0, size_df):
    #    wkt_r = WKTReader()
   #     str_adt_border = df.loc[i, 'WKT']
    #    adt_border = wkt_r.read(str_adt_border)
    #    name_adt = df.loc[i, 'name__ru']
    #    Adt(i+1, name_adt, adt_border).save()

    #print(pnt)
    #gcol = GeometryCollection(coordinates)
    #multipoligon = MultiPolygon(str(coord))
    #print(coordinates.loc[0, 'coordinates'])
    #lencor = coordinates.size-1
    #for i in range(0, 5):
        #pol = Polygon (coordinates.loc[i, 'coordinates'])
        #print(coordinates.loc[i, 'coordinates'])
        #print('            ********************                 ')
    #print(features.columns)
    #print(df.shape)
    
    #Country(1, 'Russia', pnt).save()
    
    #russia = Country.objects.create(id_country = 1, name_country = 'Россия', country_border = pnt)
    #return render(request, "database_update.html")
    return 185
    
def fill_fedo(id_country):
    data = ''
    with open(r'storage/admin_level_3.geojson') as project_file:    
        data = json.load(project_file)  

    df = pd.json_normalize(data)
    #df.info()
    
    features_df = df.loc[0, 'features']
    features = pd.DataFrame(data = features_df)
    #namefed = features.unique()
   
    #features.info()
    #features.info()
    len_f = len(features)
    #features.sort_values(by = 'name')
    #size_feat = features.size
    
    #print(size_feat)
    #print(features.shape)
    for i in range (0, len_f):
        name = features.loc[i, 'name']
        coord = features.loc[i, 'geometry']
        coordinates = pd.DataFrame(data = coord)
        pnt = GEOSGeometry(str(coord))
        #Fed_o(i, name, pnt, id_country).save()
        Fed_o(i+1, name, pnt, id_country).save()
    
    #print(pnt)
    #gcol = GeometryCollection(coordinates)
    #multipoligon = MultiPolygon(str(coord))
    #print(coordinates.loc[0, 'coordinates'])
    #lencor = coordinates.size-1
    
    #for i in range(0, 5):
        #pol = Polygon (coordinates.loc[i, 'coordinates'])
        #print(coordinates.loc[i, 'coordinates'])
        #print('            ********************                 ')
    #print(features.columns)
    #print(df.shape)
    
    #Adt(1, 'Russia', pnt).save()    

#области    
def fill_subrf(id_country):
    #df = pd.read_csv(r'storage/admin_level_2.csv', sep =';')
    #df = pd.read_json(r'storage/admin_level_2.geojson')
    #df.info()
    #col = df.columns
   # size_df = df.size
   # print(size_df)
   # for i in range (0, size_df):
    #    wkt_r = WKTReader()
   #     str_adt_border = df.loc[i, 'WKT']
    #    adt_border = wkt_r.read(str_adt_border)
    #    name_adt = df.loc[i, 'name__ru']
    #    Adt(i+1, name_adt, adt_border).save()
    data = ''
    with open(r'storage/admin_level_4.geojson') as project_file:    
        data = json.load(project_file)  

    df = pd.json_normalize(data)
    #df.info()
    
    features_df = df.loc[0, 'features']
    features = pd.DataFrame(data = features_df)
    
    #features.info()
    len_f = len(features)
    
    #size_feat = features.size
    
    #print(size_feat)
    #print(features.shape)
    for i in range (0, len_f):
        name = features.loc[i, 'name']
        coord = features.loc[i, 'geometry']
        coordinates = pd.DataFrame(data = coord)
        pnt = GEOSGeometry(str(coord))
        Subrf(i+1, name, pnt, id_country).save()    

#области    
def fill_oblasti():

    data = ''
    with open(r'storage/admin_level_4.geojson') as project_file:    
        data = json.load(project_file)  
    df = pd.json_normalize(data)
    features_df = df.loc[0, 'features']
    features = pd.DataFrame(data = features_df)
    len_f = len(features)
    for i in range (0, len_f):
        name = features.loc[i, 'name']
        coord = features.loc[i, 'geometry']
        coordinates = pd.DataFrame(data = coord)
        pnt = GEOSGeometry(str(coord))
        Oblasti(i+1, name, pnt).save() 
        
def create_ugms():
    #df = pd.read_csv(r'storage/catalog.csv', sep =';')
    #df.info()
    #k = len(df.loc[0])
    #col = df.columns
    #cat_ugms = df['Название УГМС'].unique()
    #i = 1
    #print(cat_ugms)
    
    list_ugms = ('ФГБУ Якутское УГМС', 
        'ФГБУ Камчатское УГМС',
        'ФГБУ Дальневосточное УГМС',
        'ФГБУ Мурманское УГМС',
        'ФГБУ Иркутское УГМС',
        'ФГБУ Среднесибирское УГМС',
        'ФГБУ Северо-Западное УГМС',
        'ФГБУ Приморское УГМС',
        'ФГБУ Авиаметтелеком Росгидромета',
        'ФГБУ ИПГ',
        'ФГБУ УГМС Республики Татарстан',
        'ФГБУ Обь-Иртышское УГМС',
        'ФГБУ Приволжское УГМС',
        'ФГБУ Северное УГМС',
        'ФГБУ Северо-Кавказское УГМС',
        'ФГБУ Верхне-Волжское УГМС',
        'ФГБУ Забайкальское УГМС',
        'ФГБУ Сахалинское УГМС',
        'ФГБУ Уральское УГМС',
        'ФГБУ Башкирское УГМС',
        'ФГБУ Крымское УГМС',
        'ФГБУ Западно-Сибирское УГМС',
        'ФГБУ Центральное УГМС',
        'ФГБУ Колымское УГМС',
        'ФГБУ Центрально-Черноземное УГМС',
        'ФГБУ Чукотское УГМС',
        'ФГБУ ГГИ',
        'ФГБУ ГАМЦ Росгидромета',
        'ФГБУ ГГО',
        'ФГБУ НПО ТАЙФУН',
        'ФГБУ Северо-Кавказская ВС',
        'ФГБУ СЦГМС ЧАМ',
        'ФГБУ ВГИ',
        'ФГБУ ЦАО',
        'ФГБУ ДВНИГМИ',
        'ФГБУ Ставропольская ВС',
        'ФГБУ ААНИИ')
    i=1
    for name in list_ugms:
        Ugms(i,name,1).save()
        i += 1
    #for val in cat_ugms:
        #print(val)
        #Ugms(i, val, 1).save()
        #i += 1
    #print(df.loc[0])
    #print(df.loc[0, 'Синоптический индекс станции'])
    #цикл для заполения БД, один раз заполнить и закомментить. Пока не доработан.
    #for i in range (0, 300): 
       # id_station = df.loc[i, 'serialNum']
        #if pd.isna(df.loc[i, 'Синоптический индекс станции']): 
       #     station_index = 0
       # else:
       #     station_index = df.loc[i, 'Синоптический индекс станции']
        #name_station_rus = df.loc[i, 'StationName']
        #name_station_en = ''
       # id_adt = 1
        #id_country = 1
        #id_subrf = 1
        #latitude = df.loc[i, 'Широта']
        #longitude = df.loc[i, 'Долгота']
        #geom = Point( longitude, latitude)
        #height_above_sea = ''
        #access_level = ''

        #geom = Point( fromstr('long'), fromstr('lat'))
        #WeatherStation(id_station, station_index, name_station_rus, name_station_en, id_adt, id_country, id_subrf, latitude, longitude, geom, height_above_sea, access_level).save()
        #station = WeatherStation.objects.create(id_station = id_station, station_index = station_index, name_station_rus = name_station_rus, name_station_en = name_station_en,  latitude = latitude, #longitude = longitude, geom = geom , height_above_sea = height_above_sea, access_level = access_level)
        #return station
    return list_ugms
    
def fill_climatdata():
    stations = WeatherStation.station_index.all()
    df = pd.DataFrame(stations)
    df.info()
    df = df.drop_duplicates().reset_index(drop = True)
    df.info()
    
    id_climatdata  = 1
    id_station = 23383
    timestamp_record = datetime.datetime.now().timestamp()
    temperature= 23
    pressure_stlev = 45
    wind_direction = 67
    average_wind_speed = 89
    horizontal_vizibility = 90
    clouds_height = 12
    clouds_number = 13
    special_phenomena = 14
    
    #ClimatData(id_climatdata, id_station, timestamp_record, temperature, pressure_stlev, wind_direction, average_wind_speed, horizontal_vizibility,clouds_height, clouds_number, special_phenomena).save()