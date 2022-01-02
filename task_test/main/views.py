from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Team, Profile, Task
from .serializers import UserSerializer, TeamSerializer, ProfileSerializer, TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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


# @api_view(['GET'])
# def id_from_name(request,name):
#     profile = Profile.



@api_view(['POST'])
def task_create(request):
    author_id = request.data.get("author", None)
    worker_id = request.data.get("worker", None)
    author_task = Profile.objects.get(id=author_id)
    worker_task = Profile.objects.get(id=worker_id)
    task = Task.objects.create(title=request.data.get("title"),
                               author=author_task,
                               worker=worker_task,
                               description=request.data.get("description"),
                               url=request.data.get("url"),
                               status=request.data.get("status"))
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['PUT'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    task.status = request.data.get("status")
    task.save()
    serializer = TaskSerializer(task)


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
    return Response(serializer.data[::-1])


@api_view(['GET'])
def task_list_author(request, pk):
    tasks = Task.objects.filter(author=pk)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data[::-1])


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
def profile_detail(request,pk):
    profile = Profile.objects.get(user_id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile_list_team(request, pk):
    profiles = Profile.objects.filter(team__name=pk, role="Programmer")
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

@api_view(['DELETE'])
def logout(request, format=None):
        request.user.auth_token.delete()
        return Response("Success logout")


