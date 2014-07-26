from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import loader, RequestContext

from django.views import generic

from polls.models import Question

# Create your views here.

class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "questions"

  def get_queryset(self):
    return Question.objects.all()

# via HttpResponse
# return HttpResponse("Welcome to Polls App")

# via static template ( without python code )
# return HttpResponse(template)

# via dynamic template ( with python code)
# but quite complex : should refactor later using render
# return HttpResponse(template.render(context))

# via django.shortcuts render
# return render(request, "polls/index.html", { "questions": questions })


class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"

  # pk_url_kwarg = "question_id"

class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"

def vote(request, question_id):
  question = Question.objects.get(pk=question_id)
  choice = question.choice_set.get(pk=request.POST["choice"])
  choice.votes += 1
  choice.save()
  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
