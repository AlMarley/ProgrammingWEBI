from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Question
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


class VoteView(generic.View):

    def post(self, request, question_id):

        question = get_object_or_404(Question, id=question_id)
        #print(request.POST)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes+= 1
        choice.save()
        return redirect('detail', question_id)




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

'''
def detail(request, question_id, template_name='polls/detail.html'):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question,
    }
    return render(request, template_name, context)
'''

'''
def mvotos(request, question_id, template_name='polls/mvotos.html'):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question,
    }
    return render(request, template_name, context)
'''


class MvotosView(generic.DetailView):
    template_name = 'polls/mvotos.html'
    model = Question


class MMvotosView(generic.View):

    def post(self, request, question_id):

        question = get_object_or_404(Question, id=question_id)
        #print(request.POST)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes+= 1
        choice.save()
        return redirect('mvotos', question_id)



class SobreView(generic.TemplateView):
    template_name = 'polls/sobre.html'

    def get_queryset(self):
        return redirect('sobre')




'''
def sobre(request, template_name='polls/sobre.html'):

    return render(request, template_name)



def sobre(request):
    print('sobre!')
    return HttpResponse('<br><b>Equipe:</b><br> <b>1:</b> Aldenor Júnior Torres Verçosa<br><b>2:</b> Deus')
'''
