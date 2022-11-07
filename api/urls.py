from django.urls import path
from api import views


urlpatterns = [
    path('', view=views.AboutView.as_view(), name='about-home'),
    path('about/', view=views.AboutView.as_view(), name='about'),
    path('calculation/', view=views.CalculationView.as_view(), name='calculation'),
]
