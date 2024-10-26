from django.contrib import admin
from django.urls import path, include
from tcc.views import RegisterViewSet, CreateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('login', RegisterViewSet,basename='Logins')
router.register('create',CreateViewSet,basename='Create')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
