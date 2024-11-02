from rest_framework import serializers
from .models import Food
from .models import Restorent


class FoodSerilaizer(serializers.ModelSerializer):
     class Meta:
        model = Food
        fields = '__all__'



class RestorentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Restorent
        fields = '__all__'
