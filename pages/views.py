from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginPageView(LoginView):
    template_name = 'login.html'


class SignUpPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

