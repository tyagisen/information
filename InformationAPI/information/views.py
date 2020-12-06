from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Category
    template_name = 'information/index.html'
    context_object_name = 'category'


class HomeCategoryDetail(DetailView):
    model = Category
    template_name = 'information/category_detail.html'
    # context_object_name =


class SubCategoryList(ListView):
    model = SubCategory
    template_name = 'information/sub_category.html'
    context_object_name = 'sub'


class SubCategoryDetail(DetailView):
    model = SubCategory
    template_name = 'information/sub_category_detail.html'


class InfoList(ListView):
    model = Information
    template_name = 'information/info.html'
    context_object_name = 'information'


# Api Start.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet, ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filterset_fields = ['category']


class InformationViewSet(viewsets.ModelViewSet, ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filterset_fields = ['sub_category']
