from django.test import TestCase
from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
from rest_framework.test import APIClient

class TestDoubleBooking(TestCase):
    
    client = APIClient()

    def setUp(self):
        self.customer_bob = { 
            "name":"Bob Joe",
            "no_of_guests":3,
            "booking_date":"2024-01-24",
            "booking_slot": 17
            };
        self.customer_randy = {
            "name": "Rny Jxn", 
            "no_of_guests" : 4,
            "booking_date" : "2024-01-22", 
            "booking_slot" : 15
            }
        self.customer_rilo = {
            "name":"Rilo M",
            "no_of_guests":6, 
            "booking_date":"2024-01-24", 
            "booking_slot":17
            }
        self.customer_ariel = {
            "name":"Ariel T",
            "no_of_guests":3, 
            "booking_date":"2024-01-22",
            "booking_slot":15
            };

    def test_duplicate_booking(self):
        
        serializer_bob = BookingSerializer(data=self.customer_bob);
        serializer_randy = BookingSerializer(data=self.customer_randy);
        serializer_rilo = BookingSerializer(data=self.customer_rilo);
        serializer_ariel = BookingSerializer(data=self.customer_ariel);
        
        self.assertTrue(serializer_bob.is_valid())
        serializer_bob.save();
        self.assertTrue(serializer_randy.is_valid())
        serializer_randy.save();

        self.assertFalse(serializer_rilo.is_valid())
        self.assertIn("ERROR: Slot for that time already taken. Please try a different hour or date.", serializer_rilo.errors["non_field_errors"])

        self.assertFalse(serializer_ariel.is_valid());
        self.assertIn("ERROR: Slot for that time already taken. Please try a different hour or date.", serializer_ariel.errors["non_field_errors"])
    

    def tearDown(self):
        Booking.objects.all().delete();

