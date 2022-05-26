from rest_framework.response import Response
from rest_framework import (
    status,
    views
)
from ..serializers.userSerializer import (
    UserRegistrationSerializer
)

import logging
logger = logging.getLogger(__name__)


class UserRegister(views.APIView):
    """
    description : User registration API
    created by : <email>
    """
    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        serializer_add_user_data = UserRegistrationSerializer(data=request.data)
        serializer_add_user_data.is_valid(raise_exception=True)

        created = serializer_add_user_data.user_registration(data=dict(
            user_params=serializer_add_user_data.data))

        if created is False:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'User not created'})
        else:
            return Response({'status': status.HTTP_201_CREATED, 'message': 'User created successfully'})