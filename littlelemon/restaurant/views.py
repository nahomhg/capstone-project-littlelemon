from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleItemView(RetrieveAPIView, DestroyAPIView,UpdateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]