from django import forms

from apps.todo.models import Task, Category


class AddTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'category', 'done']


class AddCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['name']
