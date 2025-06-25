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
from accounts.views import account_register, account_login, success
from page.views import page_post, post_feed
urlpatterns = [
    path('__reload__/', include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('register/', account_register, name='register'),
    path('login/', account_login, name='login'),
    path('success/', success, name='success'),
    path('post/', page_post, name='post'),
    path('feed/', post_feed, name='feed')
]
