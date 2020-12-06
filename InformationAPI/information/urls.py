from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<int:pk>/', views.HomeCategoryDetail.as_view(), name='category-detail'),
    path('info/', views.InfoList.as_view(), name='info-list'),
    path('sub/', views.SubCategoryList.as_view(), name='sub-category'),
    path('info_detail/<int:pk>/', views.SubCategoryDetail.as_view(), name='info-detail'),

]
