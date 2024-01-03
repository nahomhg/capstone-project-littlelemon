from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
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
    template_name = 'booking.html'
    
    @csrf_exempt
    def post(self,request):
        form_data_json = JSONParser().parse(request);
        form_serializer = BookingSerializer(data=form_data_json);
        if form_serializer.is_valid():
            try:
                form_serializer.save();
            except:
                print("error saving user\nError: "+str(form_serializer.errors))
                           
            return JsonResponse(form_serializer.data,status=200)
        else:
            print("invalid form"+str(form_serializer.error_messages)+"\nERROR: "+str(form_serializer.errors))
            return render(request, self.template_name, {});
