from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'public']
       labels = {'name':'', 'lang':'', 'code':''}
       widgets = {
           'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
           'code': TextInput(attrs={'placeholder': 'Код сниппета'})
       }
       # exlude указываем поля которые нужно исключить
       # fields  и exclude вместе использовать недься
       # exclude = ['lang']