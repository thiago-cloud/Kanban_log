from django.urls import path #Importando os path de Kanban_log app principal
#import views#Importando as views de users
from django.contrib.auth import views as auth_views #Essa views serve para authenticação do usuario e ela que é responsavel pela authenticação de login e senha do usuario as views_auth e o apelido da views porque tem duas iguais uma importada do Kanban_log e outra importada de user para o django saber a diferença de uma de outra na hora de usar e necessário um apelido para uma das duas.

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#Nesse caso a view ja estar pronta que no caso é a longView do django então não será necessário criar a função view.
]