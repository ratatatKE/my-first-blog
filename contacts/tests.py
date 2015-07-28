from django.test import TestCase
from contacts.models import Contact

# Create your tests here.

class ContactTests(TestCase):
    def test_str(self):
        contact=Contact(first_name='John', last_name='Smith')
        self.assertEquals(str(contact), 'John Smith')