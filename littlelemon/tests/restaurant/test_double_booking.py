from django.test import TestCase
from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
from rest_framework.test import APIClient

class TestDoubleBooking(TestCase):
    
    client = APIClient()

    def setUp(self):
        self.customer_bob = Booking.objects.create(name="Bob Joe",no_of_guests=3, booking_date="2024-01-24", booking_slot="17");
        self.customer_randy = Booking.objects.create(name="Rny Jxn", no_of_guests=4, booking_date="2024-01-22", booking_slot="15");
        self.customer_rilo = Booking.objects.create(name="Rilo M",no_of_guests=6, booking_date="2024-01-24", booking_slot="17");
        self.customer_ariel = Booking.objects.create(name="Ariel T", no_of_guests=3, booking_date="2024-01-22", booking_slot="15");


    def test_duplicate_booking(self):
        
        response = self.client.get('/api/booking/')
        serializer = BookingSerializer([self.customer_bob, self.customer_randy, self.customer_rilo, self.customer_ariel], many=True);
        print("response data ="+str(response.data))
        self.assertFormError(response.data, serializer.data)
        

    def tearDown(self):
        self.customer_bob.delete();
        self.customer_randy.delete();
        self.customer_rilo.delete();
        self.customer_ariel.delete();

