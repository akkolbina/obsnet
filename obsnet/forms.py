from django import forms
from obsnet.models import Subrf
from obsnet.models import Fed_o
from obsnet.models import Country
from obsnet.models import Ugms

class FilterForm(forms.Form):

    ch_con = [('0', '-')]
    for name_country in Country.objects.all():
        ch_c=(name_country.pk, name_country) 
        ch_con.append(ch_c)
    filter_country = forms.ChoiceField( label='Страны', choices = ch_con)

    ch = [('0', '-')]
    #text = 
    #ch.append(text)
    #ch1=[(name_subrf.pk, name_subrf) for name_subrf in Subrf.objects.all()]
    for name_subrf in Subrf.objects.all():
        ch1=(name_subrf.pk, name_subrf)
        ch.append(ch1)
    
    filter_subrf = forms.ChoiceField(label='Области', choices = ch ) 
    
    ch_fed = [('0', '-')]
    for name_fed_o in Fed_o.objects.all():
        chf=(name_fed_o.pk, name_fed_o) 
        ch_fed.append(chf)
    filter_fedo = forms.ChoiceField(label='Фед. округа', choices = ch_fed) 
    

    ch_ugms = [('0', '-')]
    for name_ugms in Ugms.objects.all():
        ch_c=(name_ugms.pk, name_ugms) 
        ch_ugms.append(ch_c)
    filter_ugms = forms.ChoiceField( label='УГМС', choices = ch_ugms)
    
    spisok_for_meteorol = [('0', '-'),('1','Срочные данные',),('2','Суточные данные'),('3','Месячные данные')]
    filter_meteorology = forms.ChoiceField(label = 'Метеорология', choices = spisok_for_meteorol)
    
    
#class AdminbdForm(forms.Form):
    