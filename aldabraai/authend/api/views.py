# django commons
from django.contrib.auth import login

# REST FRAMEWORK
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import BasicAuthentication


## KNOX
from knox.views import LoginView as KnoxLoginView


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
