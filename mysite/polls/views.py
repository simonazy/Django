from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse 

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ",".join([q.question_txt for q in latest_question_list])
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})

def detail(request, question_id):
    try:
        the_q = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    # the_q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"the_q":the_q})

# 每个view不一定非要返回新route的， 这个view就是在处理request的内容， 然后update数据；
def vote(request, question_id):
    the_question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = the_question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"the_q":the_question, "error_message":"You didn't select a choice." })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an 'HttpResponseRedirect' after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:result", args=(question_id,))) #, makes args a tuple


def results(request, question_id):
   the_question = get_object_or_404(Question, pk=question_id)
   return render(request, "polls/result.html", {"the_q":the_question})
