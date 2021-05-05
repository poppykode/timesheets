  
from django.urls import path
from .views import (
    create_project,
    get_projects,
    delete_project,
    update_project,
    restore_project,
    ##################################
    create_task,
    get_tasks,
    delete_task,
    update_task
 
)

urlpatterns = [
    path('create', create_project),
    path('all', get_projects),
    path('delete/<int:id>', delete_project),
    path('update/<int:id>', update_project),
    path('restore/<int:id>', restore_project),
    #########################################
    path('task/create', create_task),
    path('task/all', get_tasks),
    path('task/delete/<int:id>', delete_task),
    path('task/update/<int:id>', update_task),
]