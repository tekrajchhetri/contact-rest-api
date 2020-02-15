from django.shortcuts import render
from rest_framework import viewsets
from contact_rest_api import serializer
from contact_rest_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

class UserLoginAPiView(ObtainAuthToken):
    """Handle create user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ContactSerializer
    queryset = models.Contact.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","phone","address")