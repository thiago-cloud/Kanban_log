from django.contrib import admin

#Importe para o painel do django a tabela Topic criada 
from Kanban_logs.models import Topic, Entry

#Para poder registrar na tabela topic
admin.site.register(Topic)
admin.site.register(Entry)



