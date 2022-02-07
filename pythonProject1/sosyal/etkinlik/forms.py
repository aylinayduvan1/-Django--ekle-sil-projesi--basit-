from django import forms
from .models import Activate

class EtkinlikForm(forms.ModelForm):
    class Meta:
        model = Activate
        fields = ('adi', 'turu', 'kapasite', 'tarih')
