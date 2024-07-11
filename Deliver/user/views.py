from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CustomerSignUpForm, SellerSignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import User
import django.contrib.auth.views as auth_views
from django.contrib.auth import login
from user.forms import LoginForm
from django.contrib.auth import views as auth_views



class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user:login')

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'user/seller_reg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user:login')

def Logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_customer:
                return reverse('products:home')
            elif user.is_seller:
                return reverse('products:home')
        else:
            return reverse('user:login')