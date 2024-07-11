from django.urls import path
from .views import *

app_name = 'products'


urlpatterns = [
    path('',items, name='home'),
    path('details/<pk>/', details, name='detail'),
]