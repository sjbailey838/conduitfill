from django import forms
from .models import Cable, CableRun, Conduit, ConduitRun

class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'

class CableRunForm(forms.ModelForm):
    class Meta:
        model = CableRun
        fields = '__all__'

class ConduitForm(forms.ModelForm):
    class Meta:
        model = Conduit
        fields = '__all__'

class ConduitRunForm(forms.ModelForm):
    class Meta:
        model = ConduitRun
        fields = '__all__'