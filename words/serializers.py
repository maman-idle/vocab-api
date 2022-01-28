from dataclasses import fields
from rest_framework import serializers
from .models import word

class wordSerializers(serializers.ModelSerializer):
    class Meta:
        model = word

        #get id, word, and translate attributes
        fields = ('id','word','translate')