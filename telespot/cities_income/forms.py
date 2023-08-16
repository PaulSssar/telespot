from django import forms
from .models import Cities


class CityForm(forms.ModelForm):
    city_name = forms.ModelMultipleChoiceField(
        queryset=Cities.objects.all(),
        label='Город',
        widget =forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Cities
        fields = ['city_name',]






