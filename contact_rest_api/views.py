from django.shortcuts import render
from rest_framework import viewsets
from contact_rest_api import serializer
from contact_rest_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from contact_rest_api import permissions

class UserLoginAPiView(ObtainAuthToken):
    """Handle create user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","email")

class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ContactSerializer
    queryset = models.Contact.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name","phone","address")

    permission_classes = (permissions.UpdateOwnContact,IsAuthenticated)

    def perform_create(self, serializer):
        """sets logged in user profile"""
        serializer.save(user_contact=self.request.user)