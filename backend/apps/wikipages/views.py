from rest_framework import viewsets

from apps.wikipages.models import WikiPage
from apps.wikipages.serializers import WikiPageSerializer


class WikiPageViewSet(viewsets.ModelViewSet):
    queryset = WikiPage.objects.all()
    serializer_class = WikiPageSerializer
    # http_method_names = ['get', 'post']


