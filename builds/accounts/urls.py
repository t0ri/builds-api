from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: api/users/signup
    path('signup', views.sign_up, name='sign-up'),
    # ex: api/users/signin/
    path('signin', views.sign_in, name='sign-in'),
]