from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, RequestContext

from polls.models import Question

# Create your views here.

def index(request):
  template = loader.get_template("polls/index.html")
  questions = Question.objects.all()
  context = RequestContext(request, {
    "questions": questions
  })

  # via HttpResponse
  # return HttpResponse("Welcome to Polls App")

  # via static template ( without python code )
  # return HttpResponse(template)

  # via dynamic template ( with python code)
  # but quite complex : should refactor later using render
  # return HttpResponse(template.render(context))

  # via django.shortcuts render
  return render(request, "polls/index.html", { "questions": questions })

def detail(request, question_id):
  return HttpResponse("Detail of " + question_id)

def results(request, question_id):
  return HttpResponse("Results of " + question_id)

def vote(request, question_id):
  return HttpResponse("Vote of " + question_id)
