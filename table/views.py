from rest_framework.viewsets import ModelViewSet
from .serializers import TableSerializer
from .models import Table


class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer