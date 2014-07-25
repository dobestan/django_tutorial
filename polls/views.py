from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Welcome to Polls App")

def detail(request, poll_id):
  return HttpResponse("Detail of " + poll_id)

def results(request, poll_id):
  return HttpResponse("Results of " + poll_id)

def vote(request, poll_id):
  return HttpResponse("Vote of " + poll_id)
