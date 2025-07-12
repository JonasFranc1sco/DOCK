"""
URL configuration for diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import account_register, account_login, success, account_edit, home
from page.views import post_create, post_feed, user_post, post_edit, post_delete
urlpatterns = [
    path('', home, name='home'),
    path('__reload__/', include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('register/', account_register, name='register'),
    path('login/', account_login, name='login'),
    path('success/', success, name='success'),
    path('post/', post_create, name='post_create'),
    path('feed/', post_feed, name='post_feed'),
    path('myfeed/', user_post, name='user_post'),
    path('post/edit/<int:page_id>', post_edit, name='post_edit'),
    path('post/delete/<int:page_id>', post_delete, name='post_delete'),
    path('account/edit/<int:user_id>', account_edit, name="account_edit")
]
