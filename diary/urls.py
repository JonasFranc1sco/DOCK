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
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import account_register, account_login, success, account_edit, home, serve_avatar, account_logout
from page.views import feed, user_diaries, page_update, page_delete, diary_update, diary_delete, diary_create, page_add, diary_view
urlpatterns = [
    path('', home, name='home'),
    path('__reload__/', include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('register/', account_register, name='register'),
    path('login/', account_login, name='login'),
    path('logout/', account_logout, name='logout'),
    path('success/', success, name='success'),
    path('feed/', feed, name='feed'),
    path('diary/create/', diary_create, name='diary_create'),
    path('feed/personal/', user_diaries, name='user_diaries'),
    path('page/update/<int:page_id>/', page_update, name='page_update'),
    path('page/add/<int:diary_id>/', page_add, name='page_add'),
    path('page/delete/<int:page_id>/', page_delete, name='page_delete'),
    path('diary/update/<int:diary_id>/', diary_update, name='diary_update'),
    path('diary/delete/<int:diary_id>/', diary_delete, name='diary_delete'),
    path('account/edit/<int:user_id>/', account_edit, name="account_edit"),
    path('diary/view/<int:diary_id>/', diary_view, name='diary_view'),
    path('avatar/<int:user_id>/', serve_avatar, name='serve_avatar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)