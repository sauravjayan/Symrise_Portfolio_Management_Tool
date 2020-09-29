from django import forms
from .models import AdditionalInfo

class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

        