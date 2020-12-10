from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class CreateCategoryDetailForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['subcat_name',]


class CreateInformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['info_title', 'info_list']

class CategoryForm(forms.ModelForm):
    category_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Category
        fields = '__all__'

class SubCategoryForm(forms.ModelForm):
    user_category=forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),initial='')
    subcat_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = SubCategory
        fields = ['user_category','subcat_name']

class InformationForm(forms.ModelForm):
    sub_category=forms.ModelChoiceField(queryset=SubCategory.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),initial='')
    info_title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    info_list=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Information
        fields = '__all__'

class InformationListForm(forms.ModelForm):
    info_title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # info_list=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    # info_list=forms.CharField(widget=forms.R(attrs={'class':'form-control'}))
    info_list=forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Information
        fields = ['info_title','info_list']
