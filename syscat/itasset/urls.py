from django.urls import path

from . import views

app_name = 'itasset'


urlpatterns = [
# Главная страница.
    path('', views.index, name='main'),
]