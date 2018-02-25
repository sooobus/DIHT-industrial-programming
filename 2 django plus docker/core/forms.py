from django import forms

from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('title', 'text', )

class CheckDoneForm(forms.Form):
    check_done = forms.MultipleChoiceField(label="check_done", choices=ToDoItem.objects.filter(done=False), widget=forms.CheckboxSelectMultiple)
