from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate

class accountSerializer(serializers.ModelSerializer):

    #configure the return form of an account, here object account will return 3 attributes
    class Meta:
        model = Account
        fields = ('id', 'email', 'name', 'profile_pict')

class signUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'name', 'password', 'profile_pict')
        extra_kwargs = {'password': {'write_only': True}}
    
    #create new account serializer
    def create(self, validated_data):        
        account = Account.objects.create_user(
            validated_data['email'], validated_data['name'], validated_data['password']
        )
        return account

class loginSerializer(serializers.Serializer):
    #get the credentials
    email = serializers.EmailField()
    password = serializers.CharField()

    #configure the validation
    def validate(self, attrs):

        #authenticate and return account info
        account = authenticate(**attrs)
        if account and account.is_active:
            return account
        #else
        raise serializers.ValidationError("Incorrect Credentials!")

