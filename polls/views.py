from django.http import HttpResponse



def index(request):
    print('Minha Primeira View!')
    return HttpResponse('Hello, World')

def sobre(request):
    print('sobre!')
    return HttpResponse('<br><b>Equipe:</b><br> <b>1:</b> Aldenor Júnior Torres Verçosa<br><b>2:</b> Deus')