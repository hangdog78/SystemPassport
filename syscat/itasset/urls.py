from django.urls import path

from . import views

app_name = 'itasset'


urlpatterns = [
    # Главная страница.
    path('', views.index, name='main'),
    # Подробно актив
    path('itasset/<int:itasset_id>/',
         views.asset_detail,
         name='itasset_detail'),
    # Создание актива
    path('create/',
         views.asset_create, 
         name='itasset_create'),
    # Редактирование актива
    path('itasset/<int:asset_id>/edit/', views.asset_edit, name='itasset_edit'),
    # Страница со списком активов.
    path('itasset/', views.itasset_list, name='itasset_list'),
]