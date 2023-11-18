from django.shortcuts import render, redirect
from django.views.generic import View
from yuhutest.apps.tasks.models import Task
from yuhutest.apps.tasks.forms import TaskForm


class TaskView(View):
   def get(self, request, *args, **kwargs):
       tasks = Task.objects.all().order_by('-created_date')
       form = TaskForm()
       context = {'tasks': tasks, 'form': form}
       return render(request, 'index.html', context)

   def post(self, request, *args, **kwargs):
       form = TaskForm(request.POST)
       if form.is_valid():
           task_form = form.save(commit=False)
           task_form.user = request.user
           task_form.save()
       return redirect('/tasks')
