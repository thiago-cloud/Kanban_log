from django import forms
from .models import Topic, Entry

#Nesse arquivo será definido quantos campos terão cada formulário e as demais características

#Backend do formulário tópico.
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']#Campo para preencher o tópico do tipo texto
        labels = {'text': ''}#Label será do tipo text também como e não quero nenhuma o campo será vazio



class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']#Campo 
        labels = {'text': ''}#Sem labels
        widgets = {'text': forms.Textarea(attrs={'cols':80})}#Campo anotações com largura de 80 cols
