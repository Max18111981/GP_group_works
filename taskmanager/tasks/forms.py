from django import forms
from .models import Task, User, Project


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'due_date']

        widgets = {
            'project': forms.Select(attrs={
                'class': 'form-select',
                'id': 'floatingProjectSelect',
                'aria-label': 'Выбор проекта для привязки задачи',
                'required': True
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingTitle',
                'placeholder': 'Очень простая задача',
                'required': True
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingDescription',
                'placeholder': 'Нужно сделать несколько пунктов...',
                'required': True
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'floatingDueDate',
                'type': 'date',
                'required': True
            }),
        }


class TaskForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ['project', 'title', 'description', 'due_date', 'status']
            widgets = {
	        	'project': forms.Select(attrs={'class': 'form-select'}),
	        	'title': forms.TextInput(attrs={'class': 'form-control'}),
	        	'description': forms.Textarea(attrs={'class': 'form-control'}),
	        	'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
	        	'status': forms.Select(attrs={'class': 'form-select'}),
	        }


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User  # Указываем модель, с которой будет работать форма
        fields = ['username', 'email']  # Указываем поля, которые будут в форме
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project  # Указываем модель, с которой будет работать форма
        fields = ['name', 'description']  # Указываем поля, которые будут в форме
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название проекта'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание проекта'}),
        }