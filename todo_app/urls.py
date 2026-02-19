from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'), # главная страница
    path('task/create/', views.todo_create, name='todo_create'),
    path('task/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('task/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('task/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]
