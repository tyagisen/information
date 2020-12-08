from .models import *
from django import forms


class CreateCategoryDetailForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['subcat_name',]


class CreateInformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['info_title', 'info_list']

