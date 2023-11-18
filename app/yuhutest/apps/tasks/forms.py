from django import forms
from django.utils.translation import gettext_lazy as _
from yuhutest.apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')
        exclude = ('user',)
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'due_date': _('Due Date')
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'})
        }
