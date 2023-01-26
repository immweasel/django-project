from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import BookingSerializer
from .models import Booking
from django.db.models import Q
from rest_framework.response import Response

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(methods=['GET'], detail=False, url_path='booking')
    def get_georgian_rest(self, bookings):
        bookings = Booking.objects.filter(Q(restaurant__exact=2))
        data = BookingSerializer(instance=bookings, many=True).data
        return Response(data)
