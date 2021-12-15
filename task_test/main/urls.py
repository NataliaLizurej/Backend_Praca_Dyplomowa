from django.urls import path
from . import views




urlpatterns = [
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:pk>/', views.task_detail, name="task-detail"),
    path('task-create', views.task_create, name="task-create"),
    path('task-update/<str:pk>/', views.task_update, name="task-update"),
    path('task-delete/<str:pk>/', views.task_delete, name="task-delete"),
    path('task-list-worker/<str:pk>/', views.task_list_worker, name="task-list-worker"),
    path('task-list-author/<str:pk>/', views.task_list_author, name="task-list-author"),
    path('user-list/', views.user_list, name="user-list"),
    path('user-detail/<str:pk>/', views.user_detail, name="user-detail"),
    path('profile-detail/<str:pk>/', views.profile_detail, name="profile-detail"),
    path('team-list/', views.team_list, name="team-list"),
    path('profile-list-team/<str:pk>/', views.profile_list_team, name="profile-list-team"),
    path('logout/', views.logout, name="logout"),

]
