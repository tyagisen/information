from . import views
from django.urls import path
from .views import EditInformationList
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<int:pk>/', views.HomeCategoryDetail.as_view(), name='category-detail'),
    path('info/', views.InfoList.as_view(), name='info-list'),
    path('sub/', views.SubCategoryList.as_view(), name='sub-category'),
    path('info-detail/<int:pk>/', views.SubCategoryDetail.as_view(), name='info-detail'),
    path('cat-create/<int:pk>/', views.CreateCategoryDetail.as_view(), name='create-category'),
    path('add-info/<int:pk>/', views.CreateInformationDetail.as_view(), name='add-info'),
    path('list_detail/<int:pk>/', EditInformationList , name='list'),
]
