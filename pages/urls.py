from django.urls import path
from pages.views import HomePageView, LoginPageView, SignUpPageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('about/', AboutPageView.as_view(), name='about')
]