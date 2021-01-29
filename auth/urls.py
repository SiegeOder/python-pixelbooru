from django.urls import path
from . import views

app_name = 'auth'
urlpatterns = [
    path('signin', views.sign_in, name='sign_in'),
    path('signup', views.sign_up, name='sign_up'),
    path('signout', views.sign_out, name='sign_out'),
]
