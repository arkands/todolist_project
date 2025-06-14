from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_list.html', {'tasks': tasks, 'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/edit_task.html', {'form': form})

def task_filter(request, status):
    if status == 'selesai':
        tasks = Task.objects.filter(completed=True)
    elif status == 'belum':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'todolist/task_list.html', {'tasks': tasks, 'form': form})
