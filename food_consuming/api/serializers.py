from django.contrib.auth.models import User
from rest_framework import serializers
from food_consuming.models import Food, Consume


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'carbs', 'proteins', 'fats', 'price']


class ConsumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consume
        fields = ['id', 'user', 'food']
