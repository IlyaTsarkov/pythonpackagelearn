"""pythonpackagelearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from package import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='loginuser'),
    path('createnewpackage/', views.createnewpackage, name='createnewpackage'),
    path('package/<int:package_pk>', views.currentpackage, name='currentpackage'),
    path('package/<int:package_pk>/edit', views.editpackage, name='editpackage'),
    path('package/<int:package_pk>/delete', views.deletepackage, name='deletepackage'),
]

