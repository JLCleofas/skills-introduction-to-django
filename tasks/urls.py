from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('task/', views.task, name='task'),
    path('create/', views.create, name='create'),
    path('update/<int:task_id>/', views.update, name='update'),
]