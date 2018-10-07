from rest_framework import serializers

from apps.wikipages.models import WikiPage


class WikiPageSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    updated_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)

    class Meta:
        model = WikiPage
        fields = ['id', 'title', 'text', 'created_at', 'updated_at', 'is_updated']
