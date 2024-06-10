"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from OAuth.views import *

router_V1 = routers.DefaultRouter()
router_V1.register('info', UserInfoViewSet, basename="user-info")
router_V1.register('users/create', UserCreateViewSet, basename='user-create') #注意顺序
router_V1.register('users/delete', UserDeleteViewSet, basename='user-delete')
router_V1.register('users', UserViewSet)
router_V1.register('ships/author', ShipIDandNameAuthorViewSet, basename='ship-author')
router_V1.register('ships', ShipIDandNameViewSet, basename='ship')
router_V1.register('shipcrew/create', ShipCrewCreateViewSet, basename='shipcrew-create')
router_V1.register('shipcrew2/create', ShipCrewCreateViewSet2, basename='shipcrew-create2')


urlpatterns = [
    path('api/', include(router_V1.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', SuccessView.as_view(actions = {'post': 'create'}), name='token_logout'),

]
