from rest_framework.response import Response
from rest_framework import (
    status,
    views
)
from utils.common import (
    get_request_value_body,
    get_query_param_value
)
from ..serializers.todoSerializer import (
    TodoListSerializer
)
from ..models import (
    TodoList
)
import json

import logging
logger = logging.getLogger(__name__)


class CreateUserToDoList(views.APIView):
    """
    description : Add task in users Todo list
    created by : <email>
    """

    def post(self, request, *args, **kwargs):

        context = {"username": request.data['username']}

        serializer_add_user_task = TodoListSerializer(data=request.data,context=context)
        serializer_add_user_task.is_valid(raise_exception=True)

        created = serializer_add_user_task.create_task_serializer(data=dict(
            user_task_params=serializer_add_user_task.data))

        if created[0] ==  True:
            todo_list = json.loads(created[1])
            return Response({'status': status.HTTP_200_OK, 'message': 'Task added in todo list','todo_list':todo_list})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Could not able to add task in todo list'})



class GetUserToDoList(views.APIView):
    """
    description : Fetch all User Todo list
    created by : <email>
    """

    def get(self, request, *args, **kwargs):

        username = request.data['username']
        user_todo_list = TodoList.objects.get_user_todo_list(username)
        return Response(user_todo_list)


class UpdateUserToDoList(views.APIView):
    """
    description : Update to User Todo list
    created by : <email>
    """

    def post(self, request, *args, **kwargs):

        update_user_todo_list = TodoList.objects.upadte_user_todo_list(request.data)
        if update_user_todo_list == True:
            return Response({'status': status.HTTP_200_OK, 'message': 'Task updated in todo list'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Could not able to update task in todo list'})

class DeleteUserToDoList(views.APIView):
    """
    description : Delete from User Todo list
    created by : <email>
    """

    def post(self, request, *args, **kwargs):

        task_id = request.data['id']
        delete_from_todo_list = TodoList.objects.delete_user_task(task_id)
        if delete_from_todo_list == True:
            return Response({'status': status.HTTP_200_OK, 'message': 'Task deleted from todo list'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Could not able to delete task from todo list'})
