from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('email/', views.email, name='email'),
    path('post_lead/', views.post_lead, name='post-lead'),
]
