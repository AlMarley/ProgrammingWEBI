from datetime import timedelta
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('Texto da questâo', max_length=200, help_text='Informe o texto da questão.')
    pub_date = models.DateTimeField('Data de publicação Questâo', default=timezone.now)

    #Bia ajudou na solução da data e hora pre-definida.
    #creation_date = models.DateTimeField('Data de criação', default=timezone.now)

    #exemplo internet
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)


    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem


    def __str__(self):
        return self.question_text

    '''
     O property esta trasnformando o metodo em fild

     o maior_choice criado abaixo, esta gerando uma consulta no banco de dados,
     onde o self.choice_set pega o relacionamento reverso, por que não podemos
     pegar o question.choice, tem que ser o contrairo (choice_set), para que ele retorne um
     queryset. Agregando um valor e pegando o maximo desse valor, retornando um dicionario
     onde foi pego a chave.

     O return esta retornando a consulta feita pelo self.choice_set pegando o votes(valor retornado
     na linha acima) igualando a variavel maior tendo como resultado o voto maior, que é retornando
     como um object e passa pelo metodo str e temos como resultado final em string.

     *** Ajuda de BONFIM JUSTINO na solução para o retorno da choice mais votada. ***
     - Para acessar seu git segue o link -> https://github.com/bonfimjustino7
     - https://www.99freelas.com.br/user/bonfim1999

    '''

    @property
    def maior_choice(self):
        maior = self.choice_set.aggregate(models.Max('votes'))['votes__max']
        return self.choice_set.get(votes__exact=maior)





'''
    def votos(self):
        return Choice.objects.filter(question=self)
        #return Choice.objects.filter(question=self).order_by('Votos').first()
'''

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Questâo')
    choice_text = models.CharField('Texto do choice', max_length=200)
    pub_date = models.DateTimeField('Data de publicacao', default=timezone.now)
    votes = models.IntegerField('Nºde Votos',default=0)


    def was_published_recently_Choice(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem


    def __str__(self):
        return self.choice_text



'''
class timing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
'''