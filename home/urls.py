from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dynamic-style.css', views.dynamic_css, name='dynamic_css'),
]
