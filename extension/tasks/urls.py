from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
   path("", views.index, name="index"),
   path("add", views.add, name="add"),
   path("api/tasks/", views.get_tasks, name="get_tasks"), # Get a List of Tasks
   path("api/tasks/<int:id>/", views.get_task, name="get_task"), # Get a Specific Task
   path("api/tasks/create/", views.create_task, name="create_task"), # Create a New Task
   path("api/tasks/update/<int:id>/", views.update_task, name="update_task"), # Update a Task
   path("api/tasks/delete/<int:id>/", views.delete_task, name="delete_task"), # Delete a Task
]