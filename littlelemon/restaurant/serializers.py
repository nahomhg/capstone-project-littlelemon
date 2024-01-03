from .models import Booking, Menu
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu;
        fields = '__all__';

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__';
        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=['name','booking_date','booking_slot']
            )
        ];