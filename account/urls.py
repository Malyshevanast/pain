from msilib import CreateRecord
from django.urls import path, include
from .views import *

urlpatterns = [
    path('createUser/', createUser),
    path('editUser/<int:id>/', editUser),
    path('deleteUser/<int:id>/', deleteUser),
    
    path('createRecord/', createRecord),
    path('editRecord/<int:id>/', editRecord),
    path('deleteRecord/<int:id>/', deleteRecord),
    
    path('createFeedback/', createFeedback),
    path('editFeedback/<int:id>/', editFeedback),
    path('deleteFeedback/<int:id>/', deleteFeedback),
    
    path('createService/', createService),
    path('editService/<int:id>/', editService),
    path('deleteService/<int:id>/', deleteService),
    
    
    path('', account),
]