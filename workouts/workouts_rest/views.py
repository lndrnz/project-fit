from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .common.json import ModelEncoder
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
        users = UserVO.objects.all()
        return JsonResponse(users, safe=False, encoder=UserVOEncoder)
    
    return JsonResponse({"message": "No users in the database."})


@require_http_methods(["GET", "POST"])
def list_exercises(request):
    if request.method == "GET":
        exercises = Exercise.objects.all()
        return JsonResponse({"exercises": exercises}, safe=False,
                            encoder=ExerciseEncoder)
        
    else: #POST
        content = json.loads(request.body)
        try:
            exercise = Exercise.objects.create(**content)
        except Exercise.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Exercise"},
                status=400,
            )
        return JsonResponse(
            exercise,
            encoder=ExerciseEncoder,
            safe=False
        )


@require_http_methods(["GET", "POST"])
def list_workouts(request):
    if request.method == "GET":
        workouts = Workout.objects.all()
        return JsonResponse({"workouts": workouts}, safe=False,
                            encoder=WorkoutEncoder)
    else: #POST
        content = json.loads(request.body)
        try:
            workout = Workout.objects.create(**content)
        except Workout.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Workout"},
                status=400
            )
        return JsonResponse(
            workout,
            encoder=WorkoutEncoder,
            safe=False
        )
        

@require_http_methods(["DELETE", "GET", "PUT"])
def workout(request, pk):
    if request.method == "DELETE":
        count, _ = Workout.objects.filter(pk=pk).delete()
        return JsonResponse({"Deleted": count > 0})
    elif request.method == "GET":
        workouts = Workout.objects.get(pk=pk)
        return JsonResponse(workouts, safe=False,
                            encoder=WorkoutEncoder)
    else: #PUT
        try:
            Workout.objects.filter(pk=pk).update(finished=True)
            workout = Workout.objects.get(pk=pk)
            return JsonResponse(workout, encoder=WorkoutEncoder,
                                safe=False)
        except Workout.DoesNotExist:
            return JsonResponse({"message": "Workout Invalid"},
                                status=400)
            
    
