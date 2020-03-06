from django.urls import path, re_path
from . import views

urlpatterns=[
    # path('', views.login, name='login'),
    # re_path(r'^register$', views.register, name='register')
    path('register/', views.RegisterView.as_view(), name='register'),
    path('base-post/', views.BasePostView.as_view(), name='base_post'),
    path('login/', views.LoginView.as_view(), name='login'),
]
