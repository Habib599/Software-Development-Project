
from django.contrib import admin
from django.urls import path
from task.views import create_task, show_tasks, delete_task, edit_task
from category.views import create_category


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_tasks, name="show_tasks"),
    path('create_task/', create_task, name="create_task"),
    path('create_category/', create_category, name="create_category"),
    path('show_tasks/', show_tasks, name="show_tasks"),
    path('delete_tasks/<int:pk>/', delete_task, name="delete_task"),
    path('edit_tasks/<int:pk>/', edit_task, name="edit_task"),
]
