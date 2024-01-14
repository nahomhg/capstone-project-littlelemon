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
<<<<<<< HEAD
                fields=['booking_date','booking_slot'],
                message=("ERROR: Slot for that time already taken. Please try a different hour or date.")
            ),
        ];

=======
                fields=['name','booking_date','booking_slot']
            )
        ];
>>>>>>> 1d1b4c481b522e8e4531c3ae261ffd87bb398ba8
