from django.shortcuts import render, redirect

from tasks.forms import TaskCreateForm, TaskForm, UserCreateForm, ProjectCreateForm
from tasks.models import Project, User, Task, TaskStatus


def index(request):
  return render(request, 'project/index.html')

def projects(request):
  projects_list = Project.objects.all()
  return render(request, 'tasks/list.html', context={'projects': projects_list})

def performers(request):
  performers_list = User.objects.all()
  return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
  tasks_list = Task.objects.all()
  return render(request, 'tasks/list.html', context={'tasks': tasks_list})


def project(request, project_id):
  project_view = Project.objects.get(pk=project_id)
  tasks_list = Task.objects.filter(project_id=project_id)
  return render(request, 'project/details.html', context={'project': project_view, 'tasks': tasks_list})


def create_project(request):
  if request.method == 'POST':
    form = ProjectCreateForm(request.POST)
    if form.is_valid():
      project_view = form.save()  # Сохраняем проект в базе данных
      return redirect('project', project_id=project_view.id)  # Перенаправляем на страницу проекта
  else:
    form = ProjectCreateForm()
  return render(request, 'project/create.html', {'form': form})


def create_performer(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('performers')
  else:
    form = UserCreateForm()

  return render(request, 'tasks/create_performer.html', {'form': form})


def create_task(request):
  if request.method == "POST":
    form = TaskCreateForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.status = TaskStatus.objects.get(name="Новая")
      task.save()
      return redirect('tasks')
  else:
    form = TaskCreateForm()

  projects_list = Project.objects.all()
  return render(request, 'tasks/create.html', context={'form': form, 'projects': projects_list})


def task(request, task_id):
  task_view = Task.objects.get(pk=task_id)
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task_view)
    if form.is_valid():
      form.save()
      return redirect('tasks')
  else:
    form = TaskForm(instance=task_view)
  return render(request, 'tasks/details.html', {'form': form, 'task': task_view})


