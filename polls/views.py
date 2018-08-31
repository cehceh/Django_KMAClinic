from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-id')#[:5]
	# output = ', '.join([q.question_text 
	# 					for q in latest_question_list])
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	#return HttpResponse(output)
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("<h1>You're looking at question %s.</h1>" % question_id)
    
    
    #query = Question.objects.get(id=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id, id=question_id)
    #return render(request, 'polls/detail.html', {'question': question})

    context ={
    	'question': question,
    	#'query': query,
    }    

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)