from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action;
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse, Http404
from datetime import datetime
from django.core import serializers
from django.shortcuts import get_object_or_404
import json

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
    
class BookingViewSet(ModelViewSet, RetrieveUpdateDestroyAPIView, ThrottleAPIMixin, AuthenticationMixin):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        serializer = BookingSerializer(instance=self.queryset,many=True);
        return Response(serializer.data, status=200);

    @action(detail=True, methods=['GET'])
    def booking_detail(self, request, *args, **kwargs):
        reservation_date = kwargs['booking_date']
        reservation_slot = kwargs['booking_slot']
        if Validate_Date.is_date(reservation_date) and validate_time_slot(reservation_slot):
            try:
                booking = Booking.objects.filter(booking_date=reservation_date, booking_slot=reservation_slot);
                serialize_booking = BookingSerializer(instance=booking);
                return Response(data=serialize_booking.data, status=200)
            except ValidationError:
                print("Validation Error "+str(ValidationError))
            except ValueError:
                print("ERROR: Value Error "+str(ValueError));
        
        return Response({'retrieve':'data'}, status=200)


    def retrieve(self, request, *args, **kwargs):
        reservation_date = kwargs['booking_date']
        print('data kwargs = '+str(kwargs));
        if Validate_Date.is_date(reservation_date):
            try:
                bookings = Booking.objects.filter(booking_date=reservation_date);
                print('data '+str(bookings))
                serialize_booking = BookingSerializer(bookings, many=True);
                return Response(data=serialize_booking.data, status=200)
            except ValidationError:
                print("Validation Error "+str(ValidationError))
            except ValueError:
                print("ERROR: Value Error "+str(ValueError));
            except Http404:
                print("404 Error: "+str(Http404))
        
        return Response({'retrieve':'data'}, status=200)

    def create(self, request, *args, **kwargs):
        form_data_json = JSONParser().parse(request);
        form_serializer = BookingSerializer(data=form_data_json);
        if form_serializer.is_valid():
            form_serializer.save();       
            return Response(form_serializer.data,status=200)
        else:
            print("invalid form"+str(form_serializer.error_messages)+"\nERROR: "+str())
            return Response({'ERROR':f'{form_serializer.errors}'},status=400);
    
    # def list(self, request, *args, **kwargs):
    #     reservation_date = kwargs['booking_date'];  
    #     if Validate_Date.is_date(reservation_date):
    #         bookings = Booking.objects.filter(booking_date__contains=reservation_date);
    #        #print(bookings)
    #         bookings_json = serializers.serialize('json',bookings)
    #         return Response(json.loads(bookings_json),status=200);
    #     else:
    #         print("data not validating")
    #     return HttpResponse({"ERROR":"Invalid Date"},status=400);    

    # def retrieve(self, request, *args, **kwargs):
    #     booking = BookingSerializer(self.queryset, many=True);
    #     return Response(json.dumps(booking), status=200);

    # def create(self, request, *args, **kwargs):
    #     form_data_json = JSONParser().parse(request);
    #     form_serializer = BookingSerializer(data=form_data_json);
    #     if form_serializer.is_valid():
    #         try:
    #             form_serializer.save();
    #         except:
    #             print("error saving user\nError: "+str(form_serializer.errors))
                           
    #         return JsonResponse(form_serializer.data,status=200)
    #     else:
    #         print("invalid form"+str(form_serializer.error_messages)+"\nERROR: "+str(form_serializer.errors))
    #         return render(request, self.template_name, {});
def validate_time_slot(time_slot):
    return True if 10 < time_slot <= 20 else False;

    

class Validate_Date(datetime):
    def is_date(value):
        try:
            date_value = datetime.strptime(value, '%Y-%m-%d').date()
            return True;
        except ValueError:
            return False;

