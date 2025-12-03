from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Task model.
class Task(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the task name.")
    completed = models.BooleanField(default=False, help_text="Is the task completed?")
    description = models.TextField(blank=True, help_text="Enter the task description.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The time when the task was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The time when the task was last updated.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")  # <-- new

    def __str__(self):
        return f"{self.name} (Completed: {self.completed})"