from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcat_name']


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'info_title', 'info_list']
