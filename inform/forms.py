from django import forms

from inform.models import EtcMod

class ModForm(forms.ModelForm):
    
    class Meta:
        model = EtcMod
        fields = ('text',)