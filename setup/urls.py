from django.contrib import admin
from django.urls import path, include
from tcc.views import RegisterViewSet,LoginViewSet, CreateViewSet, BringNoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', RegisterViewSet,basename='Registers')
router.register('login', LoginViewSet,basename='Logins')
router.register('create',CreateViewSet,basename='Create')
router.register('bringnote',BringNoteViewSet,basename='BringNote')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
