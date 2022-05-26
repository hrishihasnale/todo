from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
import uuid
from .managers.userManager import (
    UserManager
)
from .managers.todoManager import (
    UserTodoListManager
)

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.username


class TodoList(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField(null=False)
    task = models.TextField(null=False)
    description = models.TextField(null=False)
    completed = models.BooleanField(default=False)

    objects = UserTodoListManager()

    def __str__(self):
        return self.task