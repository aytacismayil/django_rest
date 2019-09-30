from django.urls import path,include,re_path as url
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

router =routers.DefaultRouter()
router.register('xeberler',Xeberler)
router.register('category',CategoryView)
urlpatterns = [
    path('',include(router.urls)),
    url(r'^api-token-auth/',obtain_auth_token)
]
 