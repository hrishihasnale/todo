from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import (
    TodoList
)
from django.core import serializers
import logging


logger = logging.getLogger(__name__)



class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = [
            'task',
            'description',
            'completed'
        ]

    def create_task_serializer(self, data):

        try:
            data['username'] = self.context.get("username", None)
            record = TodoList.objects.create_user_task(**data)
            serialized_obj = serializers.serialize('json', [record, ])
            return True, serialized_obj

        except Exception as err:
            logging.info(err)
            return False
