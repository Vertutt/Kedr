"""
URL configuration for kedrSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings

from kedrSite.views import UserConfirmEmailView
from trees.views import TreesAPIList, TreesAPIDetails, TreesAPICoordinates
from users.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),#админка, логин admin пароль 1234
    path('api/v1/trees/',TreesAPIList.as_view(), name = 'trees'),#Список всех деревьев с их данными
    path('api/v1/trees_coordinates/',TreesAPICoordinates.as_view(), name = 'trees coordinates'),#коорды все деревьев
    path('api/v1/trees/<int:pk>/',TreesAPIDetails.as_view(), name = 'tree'),#инфа об определенном 1 дереве
    path('api/v1/user/register/', CreateUserView.as_view(), name='register'),#регистрация пользователя
    path('api/v1/auth/', include('rest_framework.urls')),#+ login/ или  logout/  вход и выход из учетки
    path('api/v1/djoser-auth/', include('djoser.urls')),#
    path('api/v1/activate/<str:uid>/<str:token>', UserConfirmEmailView.as_view()),
    re_path(r'^djoser-auth/', include('djoser.urls.authtoken')),#
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
