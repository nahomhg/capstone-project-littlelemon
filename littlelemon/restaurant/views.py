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
    
    # def get(self, request):
    #     menu_items = Menu.objects.all();
    #     serializer = MenuSerializer(menu_items, many=True);
    #     return JsonResponse(serializer.data); 

    # def post(self, request):
    #     if request.method == "POST":
    #         data = MenuSerializer(request.POST);
    #         if data.is_valid():
    #             pass;

class SingleItemView(RetrieveAPIView, DestroyAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer