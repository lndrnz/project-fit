from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import Account
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
import djwto.authentication as auth
import json

class AccountListEncoder(ModelEncoder):
    model = Account
    properties = ["first_name", "id", "username"]

class AccountDetailEncoder(ModelEncoder):
    model = Account
    properties = [
        "email",
        "first_name",
        "last_name",
        "password",
        "is_active",
        "data_joined",
        "censored",
    ]

@require_http_methods( ["GET", "POST"])
def api_list_accounts(request):
    if request.method == "GET":
        atttendees = Account.objects.all()
        return JsonResponse(
            {"accounts": atttendees},
            encoder=AccountListEncoder
        )
    else:
        try:
            content = json.loads(request.body)
            new_username = content["username"]
            new_password = content["password"]
            new_first_name = content["first_name"]
            new_last_name = content["last_name"]
            new_email = content["email"]
            account = Account.objects.create_user(
                username=new_username,
                password=new_password,
                first_name=new_first_name,
                last_name=new_last_name
            )
            account.save()
            login(request,account)
            return JsonResponse(
                account,
                encoder=AccountDetailEncoder,
                safe=False,
            )
        except Exception as response:
            response = JsonResponse(
                { "message": "The credentials are not unique. Please try a different one."
                }
            )
            response.status_code = 405
            return response

def update_censors(request, pk):
    if request.method == "PUT":
        account = Account.objects.get(id=pk)
        content = json.loads(request.body)
        new_censor = content["censored"]

        Account.objects.filter.get(id=pk)
        return JsonResponse(
            account,
            encoder=AccountDetailEncoder,
            safe=False
        )
    else:
        return JsonResponse({"message": "Your request has failed"})

@require_http_methods(["DELETE", "PUT", "GET"])
def api_show_account(request,pk):
    if request.method == "GET":
        account = Account.objects.get(id=pk)
        return JsonResponse (
            account,
            encoder=AccountDetailEncoder,
            safe=False
        )
    elif request.method =="DELETE":
        count, _= Account.objects.filter(id=pk).delete()
        Account.objects.filter(id=pk).delete()
        return JsonResponse ({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        new_username=content["username"]
        new_password = make_password(content["password"])
        new_first_name=content["first_name"]
        new_last_name=content["last_name"]
        new_email=["email"]

        Account.objects.filter(id=pk).update(
            username=new_username,
            password=new_password,
            email=new_email,
            first_name=new_first_name,
            last_name=new_first_name
        )

        account = Account.objects.get(id=pk)
        return JsonResponse (
            account,
            encoder=AccountDetailEncoder,
            safe=False,
        )