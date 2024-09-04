from django import forms
from .models import Topic

#Backend do formulário.
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']#Campos do tipo texto
        labels = {'text': ''}