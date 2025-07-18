from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'date', 'time', 'is_completed', 'user')
    list_filter = ('priority', 'is_completed', 'date')
    search_fields = ('title', 'description', 'user__username')

admin.site.register(Task, TaskAdmin)
