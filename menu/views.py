from rest_framework.viewsets import ModelViewSet
from .serializers import MenuSerializer
from .models import Menu


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer