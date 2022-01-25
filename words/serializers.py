from dataclasses import fields
from rest_framework import serializers
from .models import word

class wordSerializers(serializers.ModelSerializer):
    class Meta:
        model = word
        fields = '__all__'