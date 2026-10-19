from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/', views.dog_list, name='dog_list'),
    path('dogs/<int:pk>/', views.dog_detail, name='dog_detail'),
    path('favorites/', views.favorite_list, name='favorites'),
    path('toggle-favorite/<int:dog_id>/', views.toggle_favorite, name='toggle_favorite'),
]