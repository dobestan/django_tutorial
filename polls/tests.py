from django.test import TestCase
from django.test.client import Client

# Create your tests here.

class IndexPageTest(TestCase):
  def test_request_status_code_should_be_200(self):
    client = Client()
    response = client.get('/polls/')
    self.assertEqual(response.status_code, 200)

  def test_request_body_should_contain_welcome_to_polls_app(self):
    client = Client()
    response = client.get('/polls/')
    self.assertContains(response, "Welcome to Polls App")
