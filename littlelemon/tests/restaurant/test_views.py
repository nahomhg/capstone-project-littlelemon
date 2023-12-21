from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):

    def setUp(self):
        self.orange_juice_test = Menu.objects.create(title="Orange Juice", price=2.0,inventory=100)
        self.apple_juice_test = Menu.objects.create(title="Apple Juice", price=2.0,inventory=100)

    # Test of the serialized data is the same data we get when we query out menu items via GET request.
    def test_getall(self): 
        response = self.client.get('/api/menu/')
        serializer = MenuSerializer([self.orange_juice_test, self.apple_juice_test],many=True);
        print("data = "+str(response.data));

        self.assertEqual(response.data, serializer.data)
    
    def tearDown(self) -> None:
        self.orange_juice_test.delete();
        self.apple_juice_test.delete();
