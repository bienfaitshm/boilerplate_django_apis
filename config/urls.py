from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie
from graphene_file_upload.django import FileUploadGraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="API NAME",
        default_version='v1',
        description="documentation of apis",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bienfaitshm@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)/$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("docs/swagger/", schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path("docs/redoc/", schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('graphql/', csrf_exempt(
        jwt_cookie(
            FileUploadGraphQLView.as_view(graphiql=True)))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
