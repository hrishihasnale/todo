from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import (
    User
)
import logging


logger = logging.getLogger(__name__)



class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def user_registration(self, data):

        try:
            record = User.objects.create_user(**data)
            return True, record

        except Exception as err:
            logging.info(err)
            return False
