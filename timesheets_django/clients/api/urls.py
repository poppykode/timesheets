  
from django.urls import path
from .views import (
    create_client,
    get_clients,
    delete_client,
    update_client,
    restore_client,
    #########################################
    create_contact,
    get_contact,
    delete_contact,
    update_contact
    
)

urlpatterns = [
    path('create', create_client),
    path('all', get_clients),
    path('all/<int:id>', get_clients),
    path('delete/<int:id>', delete_client),
    path('update/<int:id>', update_client),
    path('restore/<int:id>', restore_client),
    #########################################
    path('contact/create', create_contact),
    path('contact/all', get_contact),
    path('contact/delete/<int:id>', delete_contact),
    path('contact/update/<int:id>', update_contact),
]