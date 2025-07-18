from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'created_at']  # user set in view
        fields = ['title', 'description', 'priority', 'date', 'time', 'is_completed']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'priority': forms.Select(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]),
        }
