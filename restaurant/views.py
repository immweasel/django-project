from rest_framework.viewsets import ModelViewSet
from .serializers import RestaurantSerializer, FavouriteRestaurantSerializer
from .models import Restaurant, FavouriteRestaurant
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title', 'description')

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated], url_path='add-favourite')
    def add_favourite(self, request,pk=None):
        user = request.user
        restaurant = self.queryset.get(pk=pk)
        try:
            restaurant = FavouriteRestaurant.objects.get(user=user, restaurant=restaurant)
            restaurant.delete()
            return Response({'message': 'Ресторан удалён из избранных'})
        except FavouriteRestaurant.DoesNotExist:
            FavouriteRestaurant.objects.create(user=user, restaurant=restaurant)
            return Response({'message': 'Ресторан добавлен в избранные'})

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='favourites')
    def get_favourites(self, request):
        user = request.user
        restaurant = FavouriteRestaurant.objects.filter(user=user)
        data = FavouriteRestaurantSerializer(instance=restaurant, many=True).data
        return Response(data)