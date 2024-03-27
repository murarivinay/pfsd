
from django.urls import path
from .import views


urlpatterns = [
    #path('success1/',success1,name='success1'),
    path('', views.send_email1, name='send_email1'),
]
