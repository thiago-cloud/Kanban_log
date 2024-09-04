from django.shortcuts import render
from .models import Topic


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