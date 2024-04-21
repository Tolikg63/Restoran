from django.urls import path
from . import views


urlpatterns = [
    path('', views.BaseIndex.as_view(), name='index')
]
