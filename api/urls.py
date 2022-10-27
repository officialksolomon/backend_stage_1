from rest_framework import routers
from django.urls import include, path
from api import views


urlpatterns = [
    path('', view=views.AboutView.as_view(), name='about-home'),
    path('about/', view=views.AboutView.as_view(), name='about')
]
