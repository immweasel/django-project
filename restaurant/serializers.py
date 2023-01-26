from rest_framework import serializers
from .models import Restaurant, FavouriteRestaurant
from authentification.serializers import UserSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FavouriteRestaurantSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    restaurant_data = RestaurantSerializer(source='restaurant')

    class Meta:
        model = FavouriteRestaurant
        exclude = ['user', 'recipe']