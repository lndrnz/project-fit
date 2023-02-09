from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import Account
from .common.json import ModelEncoder
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
        "date_joined",
        "username"
    ]

@require_http_methods(["GET"])
def api_user_token(request):
    if "jwt_access_token" in request.COOKIES:
        token = request.COOKIES["jwt_access_token"]
        if token:
            return JsonResponse({"token": token})
    response = JsonResponse({"token": None})
    return response


@auth.jwt_login_required
def get_some_data(request):
    token_data = request.payload
    response = JsonResponse({"token": token_data["user"]})
    return response


@auth.jwt_login_required
def check_user(request):
    if request.user is not None:
        return JsonResponse({"authenticated": request.user.is_authenticated})
    else:
        return JsonResponse({"message": "not found"})

@require_http_methods( ["GET", "POST"])
def api_list_accounts(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        return JsonResponse(
            {"accounts": accounts},
            encoder=AccountListEncoder
        )
    else:
        try:
            if request.method == "POST":
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
                    safe=False
                )
        except Exception as response:
            response = JsonResponse( {"message": "The credentials are not unique. Try another one."}
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
        return JsonResponse ({"Account is deleted.": count > 0})
    else:
        content = json.loads(request.body)
        new_username=content["username"]
        new_password = make_password(content["password"])
        new_first_name=content["first_name"]
        new_last_name=content["last_name"]
        new_email=content["email"]

        Account.objects.filter(id=pk).update(
            username=new_username,
            password=new_password,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,   
        )

        account = Account.objects.get(id=pk)
        return JsonResponse (
            account,
            encoder=AccountDetailEncoder,
            safe=False,
        )

@require_http_methods(["POST"])
def new_authenticate(request):
    new_username= request.POST["username"]
    new_password = request.POST["password"]
    user = authenticate(request, username=new_username, password=new_password )
    if user is not None:
        login(request,user)
        return JsonResponse(
            {
                "message":"User is logged in"
                }
                )
    else:
        response = JsonResponse(
            {
            "message": "The credentials are not unique. Please try a different one."
            }
        )
        response.status_code = 400
        return response

@require_http_methods(["DELETE"])
def new_logout(request):
    logout(request)
    return JsonResponse({"message": "You have been logged out."})