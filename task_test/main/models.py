from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


ROLE_CHOICES = (
    ('Programmer', 'Programmer'),
    ('Team Leader', 'Team Leader')
)


class Profile(models.Model):
    user = models.OneToOneField(User, null=None, on_delete=models.CASCADE)
    role = models.CharField(max_length=25,
                            choices=ROLE_CHOICES,
                            default='Programmer',
                            null=None)
    team = models.ForeignKey(Team, null=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


STATUS_CHOICES = (
    ('Created', 'Created'),
    ('In proccess', 'In proccess'),
    ('Done', 'Done'),
    ('Closed', 'Closed')
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, null=None, on_delete=models.CASCADE, related_name='author_task')
    worker = models.ForeignKey(Profile, null=None, on_delete=models.CASCADE, related_name='worker_task')
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=25,
                              choices=STATUS_CHOICES,
                              default='Created',
                              null=None)

    def __str__(self):
        return self.title



