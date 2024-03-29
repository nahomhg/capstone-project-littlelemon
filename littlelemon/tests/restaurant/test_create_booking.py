from django.test import TestCase
from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
from django.core import serializers
from rest_framework.test import APIClient
import datetime
import json

class CreateBookingTest(TestCase):
    
    client = APIClient()
    today_date = datetime.date.today();

    def setUp(self) -> None:
        self.booking_one = Booking.objects.create(name="Ada Lovelace", no_of_guests=5, booking_date=str(self.today_date), booking_slot=13)
        self.booking_two = Booking.objects.create(name="Rick Astley", no_of_guests=2, booking_date=str(self.today_date), booking_slot=18)

    def test_create_booking(self):
        serializer = BookingSerializer([self.booking_one, self.booking_two], many=True).data
        response = self.client.get(f'/api/bookings/{self.today_date}')
        self.assertEqual(response.status_code, 200)
        jsn = json.dumps(serializer);
        print('json data='+str(jsn))
        self.assertEqual(response.data, serializer);

    def tearDown(self) -> None:
        self.booking_one.delete();
        self.booking_two.delete();
