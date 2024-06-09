from django.shortcuts import render
from rest_framework import viewsets, status
from OAuth.models import newuser
from rest_framework.response import Response
# Create your views here.
from OAuth.serializers import UserSerializer


#只返回成功，留出接口
class SuccessView(viewsets.ModelViewSet):
    # queryset = newuser.objects.all().order_by('id')
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all().order_by('id')
    http_method_names = ['get']
    # serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        print('list_ok')
        user_info = newuser.objects.filter(id=request.user.id).values()[0]
        roles = request.user.roles
        if roles == 0:
            user_info['roles'] = ['admin']
        else:
            user_info['roles'] = ['user']

        return Response(user_info)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
