from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status


from . import models 
from . import serializers

import datetime 

from django.shortcuts import render
from .models import Link
from .serializers import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView , UpdateAPIView, DestroyAPIView

# Create your views here.
class ActiveLinkView(ListAPIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(ListAPIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class LinkListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class ListDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


