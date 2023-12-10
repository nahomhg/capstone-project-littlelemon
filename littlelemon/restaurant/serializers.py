from .models import Booking, Menu
from rest_framework.serializers import ModelSerializer


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu;
<<<<<<< HEAD
        fields = '__all__';
=======
        fields = '__all__';


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__';
>>>>>>> development
