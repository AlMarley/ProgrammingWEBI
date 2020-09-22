from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from polls.models import Question


def index(request, template_name='polls/index.html'):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, template_name, context)


'''    
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,

    }

    html = template.render(context, request)

    #print(latest_question_list)
    #print('Minha Primeira View!'

    return HttpResponse(html)
'''


def detail(request, question_id, template_name='polls/detail.html'):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question,
    }
    return render(request, template_name, context)


def mvotos(request, question_id, template_name='polls/mvotos.html'):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question,
    }
    return render(request, template_name, context)

def sobre(request):
    print('sobre!')
    return HttpResponse('<br><b>Equipe:</b><br> <b>1:</b> Aldenor Júnior Torres Verçosa<br><b>2:</b> Deus')



'''

'''