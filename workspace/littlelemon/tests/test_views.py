from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.urls import reverse
from  restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.pizza = Menu.objects.create(title='Pizza', price=6.99, inventory=4)
        self.burger = Menu.objects.create(title='Burger', price=5.99, inventory=3)
        self.pasta = Menu.objects.create(title='Pasta', price=13.99, inventory=5)
    def test_get_all(self):
        client = APIClient()
        response = client.get(reverse('restaurant:menu'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)