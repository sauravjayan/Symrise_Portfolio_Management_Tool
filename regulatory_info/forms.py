from django import forms
from .models import RegulatoryInfo

class RegulatoryInfoForm(forms.ModelForm):
    class meta:
        model = RegulatoryInfo
        fields = '__all__'