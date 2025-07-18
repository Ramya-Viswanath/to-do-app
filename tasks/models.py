from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
   # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    date = models.DateField(default=timezone.localdate)
    time = models.TimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def get_priority_color(self):
        priority = self.priority.lower()
        if priority == 'high':
            return 'red'
        elif priority == 'medium':
            return 'orange'
        else:
            return 'green'

    def __str__(self):
        return self.title
    
    def user_tasks_view(request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user).order_by('date', 'time')
            return render(request, 'tasks/user_tasks.html', {'tasks': tasks})
        else:
            return redirect('login')  # or show error