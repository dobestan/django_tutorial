from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, RequestContext

# Create your views here.

def index(request):
  template = loader.get_template("polls/index.html")

  # via HttpResponse
  # return HttpResponse("Welcome to Polls App")

  # via static template ( without python code )
  return HttpResponse(template)

def detail(request, question_id):
  return HttpResponse("Detail of " + question_id)

def results(request, question_id):
  return HttpResponse("Results of " + question_id)

def vote(request, question_id):
  return HttpResponse("Vote of " + question_id)
