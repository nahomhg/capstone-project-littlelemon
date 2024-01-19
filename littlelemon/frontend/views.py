from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from restaurant.views import MenuItemView
from restaurant.views import ThrottleAPIMixin, AuthenticationMixin, UserRateThrottle
from restaurant.serializers import BookingSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

class MenuItemsTemplate(TemplateView, ThrottleAPIMixin):
    template_name = 'index.html';
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = MenuItemView.queryset.all;
        return context

class SingeItemTemplateView(TemplateView, AuthenticationMixin, UserRateThrottle):
    template_name = 'item_detail.html';
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["item"] = MenuItemView.queryset.get(pk=kwargs["pk"]);
        except:
            context[""] = ""
        return context;
 
class BookTableTemplate(TemplateView, ThrottleAPIMixin):
    template_name = 'booking.html';
