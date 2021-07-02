from rest_framework import serializers

from .models import Feed


class FeedURLSerializer(serializers.Serializer):
    feed_url = serializers.URLField(required=True)


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('id')