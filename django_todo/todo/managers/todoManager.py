from django.db import models
from django.apps import apps
import logging
logger = logging.getLogger(__name__)



class UserTodoListManager(models.Manager):
    '''
    creating a manager for a user todo list model
    '''

    def get_queryset(self):
        return UserTodoListQuerySet(self.model, using=self._db)

    def create_user_task(self, **kwargs):
        return self.get_queryset().create_user_task(**kwargs)

    def get_user_todo_list(self, username):
        return self.get_queryset().get_user_todo_list(username)

    def upadte_user_todo_list(self, username):
        return self.get_queryset().update_user_todo_list(username)

    def delete_user_task(self, task_id):
        return self.get_queryset().delete_user_task(task_id)

class UserTodoListQuerySet(models.QuerySet):

    # Add task in users TODO List
    def create_user_task(self, **kwargs):

        user_task_serializer = kwargs['user_task_params']
        task = user_task_serializer['task']
        description = user_task_serializer['description']
        completed = user_task_serializer['completed']
        username = kwargs['username']

        mdl_todo_list = apps.get_model(app_label='todo', model_name='TodoList')

        todo_list = mdl_todo_list()
        todo_list.task = task
        todo_list.description = description
        todo_list.completed = completed
        todo_list.username = username

        todo_list.save()
        return todo_list

    # Fetch all users TODO List
    def get_user_todo_list(self, username):
        return self.filter(username=username).values('id','task','description','completed','username')

    # Update users TODO List
    def update_user_todo_list(self, data):
        try:
            check_task = self.get(username=data['username'],id=data['id'])
            if check_task:

                data._mutable = True
                if data['completed'] == 'on':
                    data['completed'] = True
                else:
                    data['completed'] = False
                data._mutable = False

                self.filter(username=data['username'],id=data['id']).update(task=data['task'],description=data['description'],completed=data['completed'])
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)
            return False

    # Delete users TODO List
    def delete_user_task(self, task_id):
        try:
            check_task = self.get(id=task_id)
            if check_task:
                self.filter(id=task_id).delete()
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)
            return False

