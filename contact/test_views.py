from django.test import TestCase
from django.urls import reverse
from .models import RequestContact
from .forms import RequestContactForm


class TestContactView(TestCase):

    def test_successful_request_contact_submission(self):
        """Test for a user requesting a contact"""
        post_data = {
           'name': 'test name',
           'email': 'test@email.com',
           'message': 'test message'
    }
    response = self.client.post(reverse('contact'), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b'Contact request received! I endeavour to respond within 2 working days.', response.content)