from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from companies import views

schema_view = get_schema_view( 
    openapi.Info( 
        title="Btooltek", 
        default_version="v1", 
        description="Btooltek CRM program API documentation", 
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(name="An-jaekgyeong", email="anjaekk@gmail.com"), 
        license=openapi.License(name=""), 
    ), 
    validators=["flex"],
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

router = DefaultRouter()
router.register(r"companies",views.CompanyAPIView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users", include("users.urls")),
    path("calendars", include("calendars.urls")),
    path("sales", include("sales.urls")),
    path("", include("router.urls")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^swagger', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^redoc', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]