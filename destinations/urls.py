from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
