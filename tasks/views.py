from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm  # Assuming you have this form defined
from django.utils.timezone import localdate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
    
class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-date', 'time')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = localdate()
        user_tasks = Task.objects.filter(user=self.request.user)
        context['pending_tasks'] = user_tasks.filter(is_completed=False, date=today).order_by('time')
        context['completed_tasks'] = user_tasks.filter(is_completed=True, date=today).order_by('time')
        context['today_date'] = today
        return context

    
class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm  # or 'fields = [...]' if no form
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # assign logged-in user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = localdate()
        context['pending_tasks'] = Task.objects.filter(is_completed=False, date=today).order_by('time')
        context['completed_tasks'] = Task.objects.filter(is_completed=True, date=today).order_by('time')
        context['today_date'] = today
        return context

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
