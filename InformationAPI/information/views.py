from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import Category
from .forms import CreateCategoryDetailForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class Home(ListView):
    model = Category
    template_name = 'information/index.html'
    context_object_name = 'category'


class HomeCategoryDetail(DetailView):
    model = Category
    template_name = 'information/category_detail.html'


class CreateCategoryDetail(CreateView):
    model = SubCategory
    form_class = CreateCategoryDetailForm
    # fields = '__all__'
    template_name = 'information/subcategory_form.html'

    def form_valid(self, form):
        form.instance.user_category_id = self.kwargs['pk']
        return super().form_valid(form)

class CreateInformationDetail(CreateView):
    model = Information
    form_class = CreateInformationForm
    template_name = 'information/information_form.html'

    def form_valid(self, form):
        form.instance.sub_category_id = self.kwargs['pk']
        return super().form_valid(form)

class SubCategoryList(ListView):
    model = SubCategory
    context_object_name = 'sub'
    template_name = 'information/sub_category.html'


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
