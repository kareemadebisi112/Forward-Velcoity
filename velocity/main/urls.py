from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('email/', views.email, name='email'),
    path('post_lead/', views.post_lead, name='post-lead'),

    # Blog
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug>/', views.blog_detail, name='blog_detail'),


    path('sitemap.xml', 
         sitemap, 
         {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'
         ),

    path('robots.txt', views.robots_txt, name='robots_txt'),
]
