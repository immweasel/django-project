from rest_framework.viewsets import ModelViewSet
from .serializers import RestaurantSerializer
from .models import Restaurant


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer