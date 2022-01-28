import imp
from rest_framework.response import Response
from .serializers import accountSerializer, signUpSerializer, loginSerializer
from rest_framework import generics, permissions, status
from django.contrib.auth.models import update_last_login
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token


class accountViewSet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = accountSerializer

    def get_object(self):
        return self.request.user


class signUpViewSet(generics.GenericAPIView):
    serializer_class = signUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        update_last_login(None, account)
        return Response({
            "account": accountSerializer(account, context=self.get_serializer_context()).data,
            "token": Token.objects.get_or_create(user=account)[0].key
        })


class loginViewSet(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data
        update_last_login(None, account)
        return Response({
            "account": accountSerializer(account, context=self.get_serializer_context()).data,
            "token": Token.objects.get_or_create(user=account)[0].key
        })

class logoutViewSet(generics.GenericAPIView):

    def post(self, request):
        #delete token
        request.user.auth_token.delete()
        
        logout(request)
        return Response({
            "message": 'Logged Out',            
        }, status=status.HTTP_200_OK)