from django.test import TestCase
from .models import User


class UserModelTests(TestCase):
    def test_is_empty(self):
        saved_user = User.objects.all()
        self.assertEqual(saved_user.count(), 0)
        self.assertEqual(saved_user.count(), 1)
