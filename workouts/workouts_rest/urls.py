from django.urls import path
from .views import list_accountsVOs

urlpatterns = [
    path("accounts/", list_accountsVOs, name="list_accounts")
]
