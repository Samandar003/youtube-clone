from django.test import TestCase
from .models import *
from .serializers import *
# Create your tests here.

class UserSerializerTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(name='John', username='John', 
        email='john@gmail.com', phone=978456245, country='America', 
        city='Los Angels', age=40, avatar="https://images.com/my_photo_04")

    def test_data(self):
        data = UserSerializer(self.user1).data
        assert data['id'] is not None
        assert data['city'] == 'Los Angels'

        