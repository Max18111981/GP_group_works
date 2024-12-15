from django.urls import path

from tasks import views


urlpatterns = [
  path('', views.index, name='index'),
  path('projects/', views.projects, name='projects'),
  path('project/<int:project_id>', views.project, name='project'),
  path('projects/create/', views.create_project, name='projects_create'),
  path('tasks/create/', views.create_task, name='tasks_create'),
  path('performers/create/', views.create_performer, name='performers_create'),
  path('performers/', views.performers, name='performers'),
  path('tasks/', views.tasks, name='tasks'),
  path('tasks/<int:task_id>/', views.task, name='task'),
]