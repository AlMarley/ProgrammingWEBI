from django.contrib import admin
from polls.models import Question, Choice
from django.utils import timezone



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


'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text', 'pub_date', 'maior_choice',)
    readonly_fields = ('maior_choice',)
'''



class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0
    readonly_fields = ('votes', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'choice_count', 'is_public', )
    search_fields = ('question_text',)
    list_filter = ('pub_date', )
    #fields = ('pub_date', 'question_text', 'was_published_recently', )
    readonly_fields = ('was_published_recently', 'maior_choice', 'is_public',)


    fieldsets = (
        ('Dados da questão', {'fields':('question_text', )}),
        ('Informações', {'fields': ('pub_date', 'was_published_recently', 'is_public',)})

    )
    inlines = (ChoiceInLine, )
    actions = ('action_pub_date_now', 'public_question', 'unpublish', )


    def choice_count(self, obj):
        return obj.choice_set.count()
    choice_count.short_description = 'Nº de Escolha'

    def action_pub_date_now(self, request, queryset):
        for question in queryset:
            question.pub_date = timezone.now()
            question.save()

    action_pub_date_now.short_description = 'Publicar Agora'


    def public_question(self, request, queryset):
        for question in queryset:
            question.is_public = True
            question.save()

    public_question.short_description = 'Publicar a Question'


    def unpublish(self, request, queryset):
        for question in queryset:
            question.is_public = False
            question.save()

    unpublish.short_description = 'Despublica a Question'



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)