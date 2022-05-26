from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)



class UserManager(models.Manager):
    '''
    creating a manager for a custom user model
    '''

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_user(self, **kwargs):
        return self.get_queryset().create_user(**kwargs)

    def get_user_obj_from_username(self, username):
        return self.get_queryset().get_user_obj_from_username(username)


class UserQuerySet(models.QuerySet):
    """
    Users QuerySet.
    """

    def create_user(self, **kwargs):

        user_data_serializer = kwargs['user_params']
        first_name = user_data_serializer['first_name']
        last_name = user_data_serializer['last_name']
        username = user_data_serializer['username']
        email = user_data_serializer['email']
        password = make_password(user_data_serializer['password'])

        mdl_user = apps.get_model(app_label='todo', model_name='User')
        user = mdl_user()
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.password = password
        user.save()

        return True, user


    def get_user_obj_from_username(self,username):
        try:
            return self.get(username=username)
        except Exception as e:
            logger.error(e)
            return False