from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'address', 'description', 'bedrooms', 'baths')
        model = House
