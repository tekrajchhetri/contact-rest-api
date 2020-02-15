from rest_framework.routers import DefaultRouter
from django.contrib import admin
from contact_rest_api import views
from django.urls import path,include
router = DefaultRouter()
router.register("contact",views.ContactViewSet)

urlpatterns = [
    path('',include(router.urls)),
]