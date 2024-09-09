from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm #Responsável por criar formulário para criação de usuário

# Create your views here.
def logout_views(request):
    """Faz Logout do usuário."""
    logout(request)#Pega o request do login e ja verifica se estar logado automaticamente
    return HttpResponseRedirect(reverse('index')) 

def register(request):
    """Faz registro de usuário."""

    # Se o usuário estiver autenticado não conseguira entrar na página de register mesmo colocando a url de register.
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method != 'POST':
        # Se for diferente de post retorne o formulário em branco.
        form = UserCreationForm()
    else:
        # Processa os dados
        form = UserCreationForm(data=request.POST)# Estou passando para dentro do parametro data o que eu recebi de POST

        # Verificando se os dados de formulário são válidos
        if form.is_valid():
            new_user = form.save()# Se forem válidos crie um novo usuario e salve no banco de dados.


            # Faz login do usuário e redireciona para página inicial.
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)# Serve para logar automaticamente após se registrar, ou seja e um retorno de athenticated_user
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)