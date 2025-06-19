from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']  # ⏰ Tambahkan deadline ke form
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
