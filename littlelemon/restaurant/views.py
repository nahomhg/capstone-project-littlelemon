from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer

class SingleItemView(RetrieveAPIView, DestroyAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer