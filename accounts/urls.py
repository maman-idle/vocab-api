import imp
from os import name
from django import views
from django.urls import path
from .views import signUpViewSet, loginViewSet, accountViewSet, logoutViewSet, bannerViewSet
from rest_framework import routers

#for request token using email and password (doesnt work with custom user)
from rest_framework.authtoken.views import obtain_auth_token


bannerRouter = routers.DefaultRouter()
bannerRouter.register('api/banner', bannerViewSet, basename='banner')

urlpatterns = [
    path('api/user/signup/', signUpViewSet.as_view()),
    path('api/user/login/', loginViewSet.as_view()),
    path('api/user/logout/', logoutViewSet.as_view()),
    path('api/user/', accountViewSet.as_view())
]

urlpatterns += bannerRouter.urls