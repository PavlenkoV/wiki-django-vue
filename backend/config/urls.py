from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
from django.conf.urls import include

from graphene_django.views import GraphQLView
from rest_framework.documentation import include_docs_urls


from config.api import api, schema_view
from apps.wikipages import views
from .schema import schema as graph_schema

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),


    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-swagger/', schema_view, name="docs"),
    path('api-docs/', include_docs_urls(title="API Docs", public=True, permission_classes=[])),
    path('api-hello/', views.HelloWorldView.as_view(), name='hello_world'),
    path('api-graphql/', GraphQLView.as_view(graphiql=True, schema=graph_schema)),

]
