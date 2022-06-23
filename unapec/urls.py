from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home' ),
    path('send_data', views.send, name='send_data')
]