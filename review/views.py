from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewSerializer
from .models import Review


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer