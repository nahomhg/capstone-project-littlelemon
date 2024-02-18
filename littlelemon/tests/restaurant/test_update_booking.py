from django.test import TestCase
from restaurant.models import Booking
from restaurant.serializers import BookingSerializer
class BookingUpdateTest(TestCase):

    def setUp(self):
        self.booking_ron = { 
            "name":"Ron Jo",
            "no_of_guests":3,
            "booking_date":"2024-02-24",
            "booking_slot": 17
            };
        self.booking_sarah = {
            "name":"Sarah Jane", 
            "no_of_guests" : 4,
            "booking_date" : "2024-02-22", 
            "booking_slot" : 18
            }

    # Testing whether we can update the data of an already existing booking. In the current iteration, I've added a 5th guest for customer 'Sarah Jane'.
    def test_getall(self): 
        serializer_ron = BookingSerializer(data=self.booking_ron);
        serializer_sarah = BookingSerializer(data=self.booking_sarah);

        self.assertTrue(serializer_ron.is_valid())
        serializer_ron.save();
        
        self.assertTrue(serializer_sarah.is_valid())
        serializer_sarah.save();
        
        self.booking_sarah["no_of_guests"] = 5;
        print("Ingoing Data: "+str(self.booking_sarah))
        response = self.client.put('/api/bookings/2024-02-22/18', data=self.booking_sarah, content_type='application/json');
        print("OUTPUT:\n1)Status code = "+str(response.status_code)+"\n2)Response Data: "+str(response))
        self.assertTrue("200", response.status_code);
    
    def tearDown(self) -> None:
        Booking.objects.all().delete();
