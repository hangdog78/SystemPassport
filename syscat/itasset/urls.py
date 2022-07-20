from django.urls import path

from . import views

app_name = 'itasset'


urlpatterns = [
    # Главная страница.
    path('', views.index, name='main'),
    # Подробно ассет
    path('itasset/<int:itasset_id>/', views.asset_detail, name='itasset_detail'),
]