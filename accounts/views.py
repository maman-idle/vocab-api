from rest_framework.response import Response
from .serializers import accountSerializer, signUpSerializer, loginSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import update_last_login


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
            "account": accountSerializer(account, context=self.get_serializer_context()).data
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
        })

