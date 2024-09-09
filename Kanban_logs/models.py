
#Para buildar essa tabela no banco de dados o comando é python .\manage.py makemigrations 

from django.db import models
from django.contrib.auth.models import User # Model padrão  User do django.

#Uma classe que herda de models.Model e nisso será gerada a tabela no banco de dados.
class Topic(models.Model):
    """Um assunto sobre o qual o usuario estar aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)# Adiciona uma data de forma automática a cada tópico.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)# Variavel dono que recebe uma chave estrangeira vinculada ao tópico que servirá para vincular cada tópico ao seu dono e assim outros usuários não ter acesso a tópicos de outro usuários.

    def __str__(self):
        """Retorna uma representação em string do modelo."""
        return self.text

class Entry(models.Model):
    """Algo específico aprendido sobre o tópico."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)# ForeignKey permite relacionar a classe Topic on_delete e obrigatorio o models.CASCADE siginifica que se for apagado um tópico toda a anotação também será apagada dando assim um efeito em cascata
    text = models.TextField()# Campo de anotações
    date_added = models.DateTimeField(auto_now_add=True)

    #Essa classe e opcional ela apenas permite que quando o django for interpretar a classe Entry no plural interprete como entries.
    class Meta:
        verbose_name_plural= 'entries'

    def __str__(self):
        """Retorna uma representação em string  do modelo."""
        return self.text[:50]+ "..." # Ele apenas retornara até 50 cracteres de anotação se passar dessa quantidade ele imprimira '...'
