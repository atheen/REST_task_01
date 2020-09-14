from rest_framework import serializers
from .models import Flight, Booking

class FlightListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination','time','price']


class BookingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight','date','id']
