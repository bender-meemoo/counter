from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('duex', views.duex),
    path('cheat', views.cheat),
    path('destroy_session', views.resetinfo)
]