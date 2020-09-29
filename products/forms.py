from django import forms
from .models import Product

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
        'expiry_date': DateInput(),
        'order_date': DateInput(),
        'arrival_date': DateInput(),
        }

class QuantityForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']


class FilterForm(forms.Form):

    pd_list = Product.objects.all()
    flv_key = []
    sol = []
    site = []
    for pd in pd_list:
        if pd.is_natural():
            li = pd.flavour_key.split('; ')
            for item in li:
                flv_key.append((item, item))
            if pd.solubility != '':
                sol.append((pd.solubility, pd.solubility))
            site.append((pd.production_site, pd.production_site))
    
    flv_key = list(sorted(set(flv_key)))
    flv_key.insert(0, ('Select all','Select all'))

    sol = list(sorted(set(sol)))
    sol.insert(0, ('Select all','Select all'))

    alc = [
        ('all', 'Select all'),
        ('less', 'Less than 0.1'),
        ('greater', 'Greater than 0.1'),
    ]
    site = list(sorted(set(site)))
    site.insert(0, ('Select all','Select all'))

    flavour_key = forms.MultipleChoiceField(choices=flv_key)
    alcohol_content = forms.ChoiceField(choices=alc,label='Alcohol content ( in % )', widget=forms.RadioSelect())
    production_site = forms.MultipleChoiceField(choices=site,widget=forms.CheckboxSelectMultiple(attrs={'id':'pro'}))
    solubility = forms.MultipleChoiceField(choices=sol,widget=forms.CheckboxSelectMultiple(attrs={'id':'sol'}))

    flavour_key.widget.attrs.update({'class':'form-control', 'size':'10', 'id':'flv'})
    alcohol_content.widget.attrs.update({'id':'alc'})
    

class NIFilterForm(forms.Form):

    pd_list = Product.objects.all()
    flv_key = []
    sol = []
    site = []
    for pd in pd_list:
        if pd.is_natural() == False:
            li = pd.flavour_key.split('; ')
            for item in li:
                flv_key.append((item, item))
            if pd.solubility != '':
                sol.append((pd.solubility, pd.solubility))
            site.append((pd.production_site, pd.production_site))
    
    flv_key = list(sorted(set(flv_key)))
    flv_key.insert(0, ('Select all','Select all'))

    sol = list(sorted(set(sol)))
    sol.insert(0, ('Select all','Select all'))

    alc = [
        ('all', 'Select all'),
        ('less', 'Less than 0.1'),
        ('greater', 'Greater than 0.1'),
    ]
    site = list(sorted(set(site)))
    site.insert(0, ('Select all','Select all'))

    flavour_key = forms.MultipleChoiceField(choices=flv_key)
    alcohol_content = forms.ChoiceField(choices=alc,label='Alcohol content ( in % )', widget=forms.RadioSelect())
    production_site = forms.MultipleChoiceField(choices=site,widget=forms.CheckboxSelectMultiple(attrs={'id':'pro'}), required=True)
    solubility = forms.MultipleChoiceField(choices=sol,widget=forms.CheckboxSelectMultiple(attrs={'id':'sol'}))

    flavour_key.widget.attrs.update({'class':'form-control', 'size':'10', 'id':'flv'})
    alcohol_content.widget.attrs.update({'id':'alc'})
    
    

