from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
from django.conf.urls import include

from rest_framework.documentation import include_docs_urls

from config.api import api, schema_view


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-swagger/', schema_view, name="docs"),
    path('api-docs/', include_docs_urls(title="API Docs", public=True, permission_classes=[])),

]
