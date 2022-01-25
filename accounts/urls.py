from django.urls import path
from .views import signUpViewSet, loginViewSet, accountViewSet

urlpatterns = [
    path('api/user/signup', signUpViewSet.as_view()),
    path('api/user/login', loginViewSet.as_view()),
    path('api/user/', accountViewSet.as_view())
]
