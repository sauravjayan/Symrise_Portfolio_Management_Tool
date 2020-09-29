from django import forms
from .models import TechnicalInfo

class TechnicalInfoForm(forms.ModelForm):
    class Meta:
        model = TechnicalInfo
        fields = '__all__'

        