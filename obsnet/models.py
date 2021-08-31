from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon 
#from django.contrib.gis.geos import Geometry


#class WeatherStation(gismodels.Model):

#    wmoid = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=256)
#    geom = gismodels.PointField()
#    objects = gismodels.Manager()

#    def __unicode__(self):
#        return self.name

class Country(models.Model):
    id_country = models.IntegerField(primary_key=True)
    name_country = models.CharField(default="", max_length=256)
    country_border = gismodels.MultiPolygonField()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)
    
    def __str__(self):
        return self.name_country

class Adt(models.Model):
    id_adt = models.IntegerField(primary_key=True)
    name_adt = models.CharField(default="", max_length=256)
    adt_border = gismodels.MultiPolygonField()
    #id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None) 
    objects_adt = gismodels.Manager()

    def __str__(self):
        return self.name_adt

class Fed_o(models.Model):
    id_fed_o = models.IntegerField(primary_key=True)
    name_fed_o= models.CharField(default="", max_length=256)
    fed_o_border = gismodels.MultiPolygonField()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None) 
    def __str__(self):
        return self.name_fed_o    

#субъекты РФ
class Subrf(models.Model):
    id_subrf = models.IntegerField(primary_key=True)
    name_subrf = models.CharField(default="", max_length=256)
    subrf_border = gismodels.MultiPolygonField()
    objects = gismodels.Manager()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None)

    #id_fed_o = models.ForeignKey(Fed_o, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.name_subrf    

class Oblasti(models.Model):
    id_oblasti = models.IntegerField(primary_key=True)
    name_oblasti = models.CharField(default="", max_length=256)
    geom = gismodels.MultiPolygonField()
    objects = gismodels.Manager()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)

    #id_fed_o = models.ForeignKey(Fed_o, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.name_oblasti   
    
class Ugms(models.Model):
    id_ugms = models.IntegerField(primary_key=True)
    name_ugms = models.CharField(default="", max_length=256)
    #ugms_border = gismodels.MultiPolygonField()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)
    #id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None)
    id_subrf = models.ForeignKey(Subrf, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.name_ugms

class WeatherStation(gismodels.Model):

    #wmoid = models.IntegerField(primary_key=True)
    #name = models.CharField(max_length=256)
    #geom = gismodels.PointField()
    #objects = gismodels.Manager()

    id_station = models.IntegerField(primary_key=True)
    station_index = models.IntegerField(default = None)
    name_station_rus = models.CharField(default="", max_length=256)
    name_station_en = models.CharField(default="", max_length=256)
    id_ugms = models.ForeignKey(Ugms, on_delete=models.CASCADE, default = None)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None) 
    id_subrf = models.ForeignKey(Subrf, on_delete=models.CASCADE, default = None)
    latitude = models.CharField(default ="", max_length=256)
    longitude = models.CharField(default ="", max_length=256)
    geom = gismodels.PointField(default ='POINT EMPTY',srid = 4326)
    objects = gismodels.Manager()
    height_above_sea = models.CharField(default="", max_length=256)
    access_level = models.CharField(default="", max_length=256)

    def __unicode__(self):
        return self.id_station

class ClimatData(models.Model):
    id_climatdata  = models.IntegerField(primary_key=True)
    id_station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, default = None)
    timestamp_record = models.CharField(default="", max_length=256)
    #tflag = models.CharField(default="", max_length=256)
    temperature= models.CharField(default="", max_length=256)
    pressure_stlev = models.CharField(default="", max_length=256)
    wind_direction = models.CharField(default="", max_length=256)
    average_wind_speed = models.CharField(default="", max_length=256)
    horizontal_vizibility = models.CharField(default="", max_length=256)
    clouds_height = models.CharField(default="", max_length=256)
    clouds_number = models.CharField(default="", max_length=256)
    special_phenomena = models.CharField(default="", max_length=256)
    def __str__(self):
        return self.id_climatdata


class Data_oper_codes(models.Model):
    id_data_oper_codes = models.IntegerField(primary_key=True)
    code = models.IntegerField(default = None)
    shortnamecode = models.CharField(default="", max_length=256)
    fullnamecode = models.CharField(default="", max_length=256)
    national_code_number = models.CharField(default="", max_length=256)
    name_in_document= models.CharField(default="", max_length=256)
    year_publication = models.IntegerField(default = None)
    data_start = models.CharField(default="", max_length=256)
    def __str__(self):
        return self.id_data_oper_codes
    
class Econfields(models.Model):
    id_econfields = models.IntegerField(primary_key=True)
    name_econfields = models.CharField(default="", max_length=256)
    econfields_border = gismodels.MultiPolygonField()
    #id_adt = models.ForeignKey(Adt, on_delete=models.CASCADE, default = None)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default = None) 
    def __str__(self):
        return self.name_econfields

