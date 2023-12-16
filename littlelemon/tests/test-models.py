from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    
    def new_menu_item(self):
        new_item = Menu.objects.create(title="Coca Cola", price=3.5,inventory=100)
        self.assertEqual(new_item.__str__(), "Coca Cola : 3.5");


