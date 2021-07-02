from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from rrs_scraper.serializers import FeedURLSerializer


class UserViewSet(viewsets.ViewSet):
    """
    The ViewSet for listing or retrieving Feeds.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = FeedURLSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FeedURLSerializer(user)
        return Response(serializer.data)