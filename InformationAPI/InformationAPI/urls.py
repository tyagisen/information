from django.contrib import admin
from django.urls import path, include
from information import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('category', views.CategoryViewSet, basename='category')
router.register('sub', views.SubCategoryViewSet, basename='sub-category')
router.register('info', views.InformationViewSet, basename='sub-information')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('home/', include('information.urls'))
]
