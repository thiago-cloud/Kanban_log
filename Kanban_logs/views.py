from django.shortcuts import render
from .models import Topic
from .models import Entry

from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404# O Http404 é página 404 padrão do django.
from django.urls import reverse
from django.contrib.auth.decorators import login_required # Essa lib do django servira para fazer as renstrições de páginas especificas quando não tiver logado.

# Um decorators serve para alterar o comportamento de uma função sem precisar modificar o código.

def index(request):

    """Página principal do Kanban_logs"""

    return render(request, 'kanban_logs/index.html') #O django vai procurar o caminho automaticamente dentro de template o render ja procura por se so dentro da pasta template

@login_required #O login_required servira para caso o usuário não esteja logado ele acessará o tópico. mais para que funcione e necessário informar ao django qual é a página de logi no arquivo seetting.py da raiz do projeto.
def topics(request):

    """´Mostrar todos os topicos"""

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')# Lista os pela data mas recente mais antes de lista ele filtra para ver se é realmente o usuário daquele tópico se for a lista é mostrada.
    context = {'topics': topics}

    return render(request, 'kanban_logs/topics.html', context)

@login_required
def topic(request, topic_id):

    """Mostra um unico assunto(tópico) e todas as suas utilidades."""

    topic = Topic.objects.get(id = topic_id)

    #Após pegar rota topic_id verifique se esse topic_id pertence a esse usuário.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')#Do mais antigo para o mais recente.
    context = {'topic':topic, 'entries': entries}

    return render(request,'kanban_logs/topic.html', context)

@login_required
def new_topic(request):

    """Adiciona um novo Tópico."""

    if request.method != 'POST':
        #Se o método não for POST nenhum dado enviado crie um formulário em branco.
        form = TopicForm()
    else:
        #Caso seja um método POST valide o formulário salve os dados e redirecione para página Tópics.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user# Verifica qual o usuário atual estar criando o tópico e a atribui o tópico criado ao usuário logado que criou.
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))#O HttpResponseRedirect serve para redirecionar para página especificada, o reverse serve para especifica qual página e que será redirecionada no caso a topics ele entende pelo name do path
    
    context = {'form': form}#Um form que recebe form.

    return render(request, 'kanban_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    """Adiciona uma nova anotação."""

    topic = Topic.objects.get(id = topic_id)#Pegando o topic do banco de dados através do id.

    #Após pegar rota topic_id verifique se esse topic_id pertence a esse usuário.
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        #Nenhum dado submetido cria um formulário em branco.
        form = EntryForm()
    else:
        #Dados de POST submetido; processa e salva os dados.
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)# O commit=False serve para não salvar de imediato no banco de dados ou seja aqui nesse caso so queremos passar os dado para variável new_entry sem salvar no banco de dados de imediato.
            new_entry.topic = topic # new_entry.topic recebe topic.
            new_entry.save()# Agora podemos salvar, por padrão o commit=true.
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))#Passando para página tópico o id.
        
    context  = {'topic':topic, 'form':form}#Passando no contexto o topico e o form new_entry.

    return render(request, 'kanban_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    
    """Edita uma entrada(anotação) existente."""

    entry = Entry.objects.get(id=entry_id)#Pegando o objeto entry(anotação) pelo id no banco de dados.
    topic = entry.topic#Lembrando que dentro do entry temos o topic sendo assim aqui estamos pegando topic.

    #Após pegar rota topic_id verifique se esse topic_id pertence a esse usuário.
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)#Pegando o formulário já existente ou seja preechido para poder editar.

    else:
        #Dados post enviados processado e validando os dados
        form = EntryForm(instance=entry, data = request.POST)#Pegando os dados que foram editados do formulário e atualizando com data request.POST
        if form.is_valid():
            form.save()#Salvando o form já editado após ser preechido e válidado.
        return HttpResponseRedirect(reverse('topic', args=[topic.id]))#Redirecionando para página topic como a página tópico exige no arquivo urls na rota o topic_id então temos que passar como agumento toda vez que redirecionarmos para topic.

    context = {'entry':entry, 'topic':topic, 'form':form}#Lembrando que o context serve para que independente da requisição será passado na criação da página esses 3 contexto

    return render(request, 'kanban_logs/edit_entry.html', context)