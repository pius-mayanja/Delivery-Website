from django.urls import path 
from .views import *


app_name = 'user'

urlpatterns = [
    path("signup/",CustomerSignUpView.as_view(), name="signup"),
    path("seller-signup/",SellerSignUpView.as_view(), name="reg"),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', Logout_view , name='logout'),
]

   

