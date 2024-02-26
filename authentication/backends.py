import jwt
from rest_framework import authentication, exceptions
from contactsapi.settings import JWT_SECRET_KEY
from .serializers import User
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split('')

        try:
            payload = jwt.decode(token, JWT_SECRET_KEY)
            user = User.objects.get(user_name=payload['user_name'])
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid')
        return super().authenticate(request)