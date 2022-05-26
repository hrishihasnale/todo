from django.urls import path
from .views import (
    todoViews,
    userViews,
    templateViews
)

urlpatterns = [

    # Template views
    path("create_task/", templateViews.create_task, name="create_task"),
    path("read_task/", templateViews.read_task, name="read_task"),
    path("update_task/", templateViews.update_task, name="update_task"),
    path("dalete_task/", templateViews.dalete_task, name="dalete_task"),

    # API views
    path('create_user/', userViews.UserRegister.as_view()),
    path('create/', todoViews.CreateUserToDoList.as_view()),
    path('get_user_list/', todoViews.GetUserToDoList.as_view()),
    path('update/', todoViews.UpdateUserToDoList.as_view()),
    path('delete/', todoViews.DeleteUserToDoList.as_view()),
]