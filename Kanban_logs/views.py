from django.shortcuts import render
from .models import Topic

from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Página principal do Kanban_logs"""
    return render(request, 'kanban_logs/index.html') #O django vai procurar o caminho automaticamente dentro de template o render ja procura por se so dentro da pasta template



def topics(request):
    """´Mostrar todos os topicos"""

    topics = Topic.objects.order_by('date_added')#Começar a listar a partir da data mas recente em ordem
    context = {'topics': topics}
    return render(request, 'kanban_logs/topics.html', context)

def topic(request, topic_id):
    """Mostra um unico assunto e todas as suas utilidades"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')#Do mais antigo para o mais recente
    context = {'topic':topic, 'entries': entries}
    return render(request,'kanban_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo Tópico."""
    if request.method != 'POST':
        #Se o método não for POST nenhum dado enviado crie um formulário em branco
        form = TopicForm()
    else:
        #Caso seja um método POST valide o formulário salve os dados e redirecione para página Tópics
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))#O HttpResponseRedirect serve para redirecionar para página especificada, o reverse serve para especifica qual página e que será redirecionada no caso a topics ele entende pelo name do path
    context = {'form': form}#Um form que recebe form
    return render(request, 'kanban_logs/new_topic.html', context)