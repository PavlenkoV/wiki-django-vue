from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend

from apps.wikipages.models import WikiPage
from apps.wikipages.serializers import WikiPageSerializer, HelloNameSerializer




class WikiPageViewSet(viewsets.ModelViewSet):
    queryset = WikiPage.objects.all()
    serializer_class = WikiPageSerializer
    # http_method_names = ['get', 'post']
    # it's already added to settings.py!
    # filter_backends = (DjangoFilterBackend,)
    # http://0.0.0.0:8000/api/wikipages?title=First%20title&format=json
    filterset_fields = ('title',)


class HelloWorldView(GenericAPIView):
    serializer_class = HelloNameSerializer

    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        context = {'allowed_names': ['Vitaliy', 'Vasya']}
        serializer = HelloNameSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Hello {}!".format(name)})

