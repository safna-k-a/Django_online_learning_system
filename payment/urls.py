from django.urls import path
from payment import views


urlpatterns = [
    path('app_create', views.app_create, name='app_create'),
    path('charge/<int:id><int:pk>', views.app_charge, name='app_charge'),
]
