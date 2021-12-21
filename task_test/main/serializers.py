from .models import User, Team, Profile, Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', default='')
    team = serializers.CharField(source='team.name', default='')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'team', 'role']


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    worker = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'author', 'worker', 'description', 'url', 'status']


