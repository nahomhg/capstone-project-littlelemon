from django.test import TestCase
from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
import datetime

class MakeBookingTest(TestCase):
    
    def setUp(self) -> None:
        self.booking_one = Booking.objects.create(name="Ada Lovelace", no_of_guests=5, booking_date=datetime.datetime.now())
        self.booking_two = Booking.objects.create(name="Rick Astley", no_of_guests=2, booking_date=datetime.datetime.now())
    
    def test_getall_bookings(self):
        response = self.client.get('/api/booking/')
        serializer = BookingSerializer([self.booking_one, self.booking_two], many=True)
        print(str(response.data))
        self.assertEqual(response.data, serializer.data);

    def tearDown(self) -> None:
        self.booking_one.delete();
        self.booking_two.delete();