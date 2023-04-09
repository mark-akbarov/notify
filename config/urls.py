# Django
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from .swagger_schema import schema_view

# Project
from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/notify/', include('notify.urls')),
    path('api/v1/stats/', include('stats.urls')),
    path('api/v1/teams/', include('teams.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# swagger configuration
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]