from rest_framework import serializers
from .models import ShopList


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopList
        fields = '__all__'
