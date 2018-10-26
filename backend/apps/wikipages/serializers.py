from rest_framework import serializers

from apps.wikipages.models import WikiPage


class WikiPageSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)
    updated_at = serializers.DateTimeField(format='%H:%M %d.%m.%Y', read_only=True)

    class Meta:
        model = WikiPage
        fields = ['id', 'title', 'text', 'created_at', 'updated_at', 'is_updated']


class HelloNameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def validate_name(self, name):
        """
        Check that the name has v.
        """
        if name not in self.context.get("allowed_names", []):
            raise serializers.ValidationError("The name should be {}!".format(self.context.get("allowed_names", [])))
        return name
