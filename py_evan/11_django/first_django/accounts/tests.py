from django.test import TestCase

from .models import User


# Create your tests here.
class Test(TestCase):

    def test_get_user(self):
        users = User.objects.get(id=1)
        print(users.count())
