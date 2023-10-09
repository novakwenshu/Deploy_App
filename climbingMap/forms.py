from typing import Any
from django import forms
from .models import ClimbingArea
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AddAreaForm(ModelForm):
    class Meta:
        model = ClimbingArea
        fields = ['area_name',
                  'type_of_climbing',
                  'rock_type',
                  'description']
    def clean_area_name(self):
        data = self.cleaned_data['area_name']
        if len(data) > 100:
            raise ValidationError(_('Invalid Area Name: Too long'))
        return data
    
    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) > 2000:
            raise ValidationError(_('Invalid Description: Too long'))
        return data
