from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from tasks.models import Task

@login_required
def dashboard(request):
    today_date = date.today().strftime("%A, %B %d, %Y")
    user_tasks = Task.objects.filter(user=request.user)
    
    pending_count = user_tasks.filter(is_completed=False).count()
    completed_count = user_tasks.filter(is_completed=True).count()

    context = {
        'today_date': today_date,
        'pending_count': pending_count,
        'completed_count': completed_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

    
