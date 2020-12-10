from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import Category
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User
class Home(View):
    # model = Category
    template_name = 'information/index.html'
    # context_object_name = 'category'

    def get(self, request):
        context = {
            'form': CategoryForm(),
            'category': Category.objects.all(),
            # 'sub':SubCategory.objects.all()
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            # messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('home')
        else:
            # messages.add_message(request, messages.ERROR, "Sory error occured")
            return redirect('home')

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

class SubCategoryList(View):

    # model = SubCategory
    template_name = 'information/sub_category.html'
    # context_object_name = 'sub'

    def get(self, request):
        context = {
            'form': SubCategoryForm(),
            'sub': SubCategory.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            # messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('sub-category')
        else:
            # messages.add_message(request, messages.ERROR, "Sory error occured")
            return redirect('sub-category')


class SubCategoryDetail(DetailView):
    model = SubCategory
    template_name = 'information/sub_category_detail.html'


class InfoList(View):
    # model = Information
    template_name = 'information/info.html'
    # context_object_name = 'information'

    def get(self, request):
        context = {
            'form': InformationForm(),
            'information': Information.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = InformationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            # messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('info-list')
        else:
            # messages.add_message(request, messages.ERROR, "Sory error occured")
            return redirect('info-list')

def EditInformationList(request, pk):

    data = Information.objects.get(pk=pk)
    form= InformationListForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        # messages.add_message(request, messages.SUCCESS, "Created Successfully")
        return redirect('info-list')
    context = {
        'form': form
    }
    return render(request, 'information/info_list.html', context)



# Api Start.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet, ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    # filterset_fields = ['category']


class InformationViewSet(viewsets.ModelViewSet, ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filterset_fields = ['sub_category']
