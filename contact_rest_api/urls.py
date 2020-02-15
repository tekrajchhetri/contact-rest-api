from rest_framework.routers import DefaultRouter
from django.contrib import admin
from contact_rest_api import views
from django.urls import path,include
router = DefaultRouter()
router.register("contact",views.ContactViewSet)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginAPiView.as_view()),
]