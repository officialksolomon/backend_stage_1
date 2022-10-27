from django.urls import path
from api import views


urlpatterns = [
    path('', view=views.AboutView.as_view(), name='about-home'),
    path('about/', view=views.AboutView.as_view(), name='about')
]
