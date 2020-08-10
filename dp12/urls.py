"""dp12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
import dp12app
from dp12app import views,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name="base"),
    path('',views.home,name="home"),
    path('dp12app/',include("dp12app.urls")),
    path('post_demo/',views.post_demo,name="post_demo"),
]
