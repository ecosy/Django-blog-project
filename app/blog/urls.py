from django.urls import path, re_path
from . import views

# app_name='blog'
urlpatterns=[
    # path('', views.login, name='login'),
    # re_path(r'^register$', views.register, name='register')
    path('register/', views.register, name='register'),
    path('base-post/', views.base_post, name='base_post'),
    path('login/', views.login, name='login'),
]
