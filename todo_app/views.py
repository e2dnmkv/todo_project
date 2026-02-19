from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def todo_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})

def todo_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_app/todo_detail.html', {'task': task})

def todo_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/todo_form.html', {'form': form, 'title': 'Новая задача'})

def todo_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/todo_form.html', {'form': form, 'title': 'Редактирование задачи'})

def todo_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_detail.html', {'task': task, 'confirm_delete': True})
