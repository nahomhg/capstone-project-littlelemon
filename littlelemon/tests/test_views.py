from django.test import TestCase
from restaurant.models import Menu

from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Orange Juice", price=2.0,inventory=100)
        Menu.objects.create(title="Apple Juice", price=2.0,inventory=100)
      

    def test_getall(self):
        response = self.client.get('/api/menu/')
        serializer = MenuSerializer(Menu.objects.all(),many=True);
        print("data = "+str(response.data));

        self.assertEqual(response.data, serializer.data)
    
