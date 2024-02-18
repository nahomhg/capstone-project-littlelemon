from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action;
from datetime import datetime, date
from django.shortcuts import get_object_or_404

# Create your views here.
class ThrottleAPIMixin:
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

class AuthenticationMixin:
    permission_classes = [IsAuthenticated]

class MenuItemView(ListCreateAPIView, ThrottleAPIMixin):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    
class SingleItemView(RetrieveUpdateDestroyAPIView, ThrottleAPIMixin, AuthenticationMixin):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    

class BookingCreate(ListCreateAPIView):
    queryset = Booking.objects.filter(booking_date__contains=date.today());
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        form_data_json = JSONParser().parse(request);
        form_serializer = BookingSerializer(data=form_data_json);
        if form_serializer.is_valid():
            form_serializer.save();      
            return Response(form_serializer.data, status=200)
        else:
            return Response({'ERROR':f'{form_serializer.errors}'},status=403);


class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer;
    
    def get_object(self):
        from django.core.serializers import serialize
        reservation_date = self.kwargs['booking_date']
        reservation_slot = self.kwargs['booking_slot']
        self.queryset = get_object_or_404(Booking, booking_date=reservation_date, booking_slot=reservation_slot);
        return self.queryset;

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs);

class Validate_Date(datetime):
    
    @staticmethod
    def is_valid_date(date_str):
        curr_date = datetime.today().date()
        if date_str >= str(curr_date):
            return True;
        else:
            return False;
    
    def validate_time_slot(time_slot):
        if 10 < int(time_slot) <= 20:
            return True
        else:
            return False;
       
