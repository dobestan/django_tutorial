from django.test import TestCase
from django.test.client import Client

from django.utils import timezone

from polls.models import Question
# Create your tests here.

class IndexPageTest(TestCase):
  def setUp(self):
    self.client = Client()
    self.response = self.client.get('/polls/')

  def test_request_status_code_should_be_200(self):
    self.assertEqual(self.response.status_code, 200)

  def test_request_body_should_contain_welcome_to_polls_app(self):
    self.assertContains(self.response, "Welcome to Polls App")

class DetailPageTest(TestCase):
  def setUp(self):
    # create database
    q = Question()
    q.title = "New Question"
    q.pub_date = timezone.now()
    q.save()

    q.choice_set.create(title="First Choice")
    q.choice_set.create(title="Second Choice")
    q.choice_set.create(title="Third Choice")

    self.client = Client()
    self.response = self.client.get('/polls/' + str(q.id) + '/')

  def test_request_status_code_should_be_200(self):
    self.assertEqual(self.response.status_code, 200)

  def test_request_body_should_contain_choices(self):
    self.assertContains(self.response, "First Choice")
    self.assertContains(self.response, "Second Choice")
    self.assertContains(self.response, "Third Choice")

class ResultsPageTest(TestCase):
  def setUp(self):
    # create database
    self.q = Question()
    self.q.title = "New Question"
    self.q.pub_date = timezone.now()
    self.q.save()

    self.c1 = self.q.choice_set.create(title="First Choice", votes=123)
    self.c2 = self.q.choice_set.create(title="Second Choice", votes=456)
    self.c3 = self.q.choice_set.create(title="Third Choice", votes=567)

    self.client = Client()
    self.response = self.client.get('/polls/' + str(self.q.id) + '/results/')

  def test_request_status_code_should_be_200(self):
    self.assertEqual(self.response.status_code, 200)

  def test_request_body_should_contain_choices(self):
    self.assertContains(self.response, self.c1.votes)
    self.assertContains(self.response, self.c2.votes)
    self.assertContains(self.response, self.c3.votes)

    self.assertNotContains(self.response, "789")
