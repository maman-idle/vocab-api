from rest_framework.response import Response
from .serializers import accountSerializer, signUpSerializer, loginSerializer, bannerSerializer
from rest_framework import generics, permissions, status, viewsets
from django.contrib.auth.models import update_last_login
from django.contrib.auth import logout
from .models import BannerBackground

#Token Auth
from rest_framework.authtoken.models import Token

#Media uploader
from rest_framework.parsers import MultiPartParser, JSONParser
from cloudinary import uploader

class accountViewSet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = accountSerializer

    def get_object(self):
        return self.request.user


class signUpViewSet(generics.GenericAPIView):
    serializer_class = signUpSerializer

    #enable end-point to process image
    parser_classes = (
        MultiPartParser,
        JSONParser
    )

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

class bannerViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = bannerSerializer

    def get_queryset(self):
        return BannerBackground.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()