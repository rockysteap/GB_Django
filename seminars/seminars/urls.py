"""
URL configuration for seminars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seminar1/', include('s1_app.urls')),
    path('seminar1/', include('s1_game_app.urls')),
    path('seminar2/', include('s2_app1_coin_app.urls')),
    path('seminar2/', include('s2_app2_article_app.urls')),
    path('seminar3/', include('s3_app1_app.urls')),
    path('seminar3/', include('s3_app2_game_app.urls')),
    path('seminar3/', include('s3_app3_article_app.urls')),
]
