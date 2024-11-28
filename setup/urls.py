from django.contrib import admin
from django.urls import path, include
from tcc.views import RegisterViewSet,LoginViewSet, CreateViewSet, BringNoteViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='API Documentation',
        default_version='v1',
        description="API documentation for a project manager",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.locas"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register('register', RegisterViewSet,basename='Registers')
router.register('login', LoginViewSet,basename='Logins')
router.register('create',CreateViewSet,basename='Create')
router.register('bringnote',BringNoteViewSet,basename='BringNote')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
