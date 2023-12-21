from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
class MenuItemTest(TestCase):
    
    def setUp(self) -> None:
        self.new_item_cola = Menu.objects.create(title="Coca Cola", price=3.5,inventory=100)
        self.new_item_fanta = Menu.objects.create(title="Fanta", price=3,inventory=100)

    def new_menu_item(self):
        self.assertEqual(self.new_item_cola.__str__(), "Coca Cola : 3.5");
        self.assertEqual(self.new_item_fanta.__str__(), "Fanta : 3");

    def tearDown(self) -> None:
        self.new_item_cola.delete();
        self.new_item_fanta.delete();



