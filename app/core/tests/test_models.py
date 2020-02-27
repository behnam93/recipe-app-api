from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_new_use_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
