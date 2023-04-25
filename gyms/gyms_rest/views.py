from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import UserVO, Exercise, Workout

class UserVOEncoder(ModelEncoder):
    model = UserVO
    properties = ["user_name"]

class ExerciseEncoder(ModelEncoder):
    model = Exercise
    properties = ["name", "description", "sets", "reps", "weight"]

class WorkoutEncoder(ModelEncoder):
    model = Workout
    properties = ["name", "description","duration","difficulty", "data_created", "exercise", "user"]
    encoders = {"exercise": ExerciseEncoder(), "user": UserVOEncoder()}

@require_http_methods(["GET"])
def list_accountsVOs(request):
    if request.method == "GET":
        users = UserVO.object.all()
        return JsonResponse(users, safe=False, encoder=UserVOEncoder)
    else:
        return JsonResponse({"message": "No users in the database."})

@require_http_methods(["GET"])
def list_exercises(request):
    if request.method == "GET":
        exercises = Exercise.objects.all()
        return JsonResponse(exercises, safe=False, encoder=ExerciseEncoder)
    else:
        return JsonResponse({"message": "No exercises in the database."})

