from django.urls import path
from .views import list_accountsVOs, list_exercises, list_workouts

urlpatterns = [
    path("accounts/", list_accountsVOs, name="list_accounts"),
    path("exercises/", list_exercises, name="list_exercises"),
    path("workouts/",list_workouts, name="list_workouts"),
    
    
]
