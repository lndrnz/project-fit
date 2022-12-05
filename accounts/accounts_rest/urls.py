from django.urls import path
from accounts_rest.views import api_list_accounts, api_show_account, update_censors, new_authenticate, new_logout, api_user_token,get_some_data,check_user

urlpatterns = [
    path("login/", new_authenticate, name="login"),
    path("logout/", new_logout, name="logout"),
    path("censor/<int:pk>", update_censors, name="censors"),
    path("accounts_list/", api_list_accounts, name="accounts_list"),
    path("accounts/<int:pk>", api_show_account, name="accounts_detail"),
    path("tokens/mine/", api_user_token, name="token"),
    path("get/token/", get_some_data, name="get_token"),
    path("check/", check_user, name="check"),
]
