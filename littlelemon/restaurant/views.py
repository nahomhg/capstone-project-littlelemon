from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response
from django.http import HttpResponse
from datetime import datetime
from django.core import serializers
import json

# Create your views here.
class ThrottleAPIMixin:
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

class AuthenticationMixin:
    permission_classes = [IsAuthenticated]

class MenuItemView(ListCreateAPIView, ThrottleAPIMixin, AuthenticationMixin):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    

class SingleItemView(RetrieveUpdateDestroyAPIView, ThrottleAPIMixin, AuthenticationMixin):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet, RetrieveUpdateDestroyAPIView , ThrottleAPIMixin, AuthenticationMixin):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer

    def retrieve(self, request, *args, **kwargs):
        reservation_date = kwargs['booking_date'];
        if Validate_Date.is_date(reservation_date):
            bookings = Booking.objects.filter(booking_date__contains=reservation_date);
            bookings_json = serializers.serialize('json',bookings)
            return Response(json.loads(bookings_json),status=200);
        return HttpResponse({"ERROR":"Invalid Date"},status=400)
    

class Validate_Date(datetime):
    def is_date(value):
        try:
            date_value = datetime.strptime(value, '%Y-%m-%d').date()
            return True;
        except ValueError:
            return False;