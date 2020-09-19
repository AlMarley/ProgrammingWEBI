from datetime import timedelta
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('Texto da questâo', max_length=200, help_text='Informe o texto da questão.')
    pub_date = models.DateTimeField('Data de publicação Questâo', default=timezone.now)
    #creation_date = models.DateTimeField('Data de criação', default=timezone.now)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)



    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem



    def __str__(self):
        return self.question_text

    def maior_choice(self):
        maior = self.choice_set.aggregate(models.Max('votes'))['votes__max']
        return self.choice_set.filter(votes__exact=maior)


    def votos(self):
        return Choice.objects.filter(question=self)
        #return Choice.objects.filter(question=self).order_by('Votos').first()


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