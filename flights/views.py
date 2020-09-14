from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import BookingListSerializers,FlightListSerializers

from django.http import JsonResponse
from datetime import date as dates

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializers


class BookingListView(ListAPIView):

    queryset = Booking.objects.filter(date__gte=(dates.today()))
    serializer_class = BookingListSerializers
