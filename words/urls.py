import imp
from django.db import router
from rest_framework import routers
from .views import wordViewSet

#setup the default router from rest_framework
router = routers.DefaultRouter()

#setup the path to default router
router.register('api/words', wordViewSet, basename='Words')

#assign the urlpatterns
urlpatterns = router.urls