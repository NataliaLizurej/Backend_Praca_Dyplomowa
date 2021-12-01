from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Team, Profile, Task
from .serializers import UserSerializer, TeamSerializer, ProfileSerializer, TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.decorators import authentication_classes
# from rest_framework.decorators import permission_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Task succesfully delete!")


@api_view(['GET'])
def task_list_worker(request, pk):
    tasks = Task.objects.filter(worker=pk)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_list_author(request, pk):
    tasks = Task.objects.filter(author=pk)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request,pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile_list_team(request, pk):
    profiles = Profile.objects.filter(team=pk)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def logout(request, format=None):
        request.user.auth_token.delete()
        return Response("Success logout")
