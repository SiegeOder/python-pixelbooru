from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view, name='post'),
    path('<int:id>/comment', views.comment, name='comment'),
    path('create', views.create, name='create')
]
