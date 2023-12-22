from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView

# Create your views here.

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated];
    
class MenuItemsTemplate(TemplateView):
    template_name = 'index.html';
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = MenuItemView.queryset.all;
        return context
    

class SingleItemView(RetrieveAPIView, DestroyAPIView,UpdateAPIView):
    queryset = Menu.objects.all();
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated]



class SingeItemTemplateView(TemplateView):
    template_name = 'item_detail.html';
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = MenuItemView.queryset.get(pk=kwargs["pk"]);
        return context;

    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]