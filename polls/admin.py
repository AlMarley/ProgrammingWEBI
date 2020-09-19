from django.contrib import admin
from polls.models import Question, Choice



'''
 class herdada de admin.ModelAdmin no qual estamos editando e registrando o question recebendo o modelquestion
 logo vai ter o questionAdmin criado abaixo.
 
 definindo os filds(os que eu tenho em models, adicionando o metedo criado 'maior_choice').
 readonly_filds: transforma o fild apenas para leitura (Logo você não poderá editar), depois do igual ele
 definindo qual vai ser esse fild que será pego automaticamente. 
 
 *** Ajuda de BONFIM JUSTINO na solução para o retorno da choice mais votada. ***
 - Para acessar seu git segue o link -> https://github.com/bonfimjustino7
 - https://www.99freelas.com.br/user/bonfim1999
'''

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text', 'pub_date', 'maior_choice',)
    readonly_fields = ('maior_choice',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)