from rest_framework import routers
from apps.users.views import UserViewSet
from apps.wikipages.views import WikiPageViewSet
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)

# WikiPages API
api.register(r'wikipages', WikiPageViewSet)

# Swagger
schema_view = get_schema_view(title='API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
