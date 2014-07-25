from django.test import TestCase
from django.test.client import Client

# Create your tests here.

class IndexPageTest(TestCase):
  def setUp(self):
    self.client = Client()
    self.response = self.client.get('/polls/')

  def test_request_status_code_should_be_200(self):
    self.assertEqual(self.response.status_code, 200)

  def test_request_body_should_contain_welcome_to_polls_app(self):
    self.assertContains(self.response, "Welcome to Polls App")
