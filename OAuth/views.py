from django.shortcuts import render
from rest_framework import viewsets, status
from OAuth.models import (newuser, Ship, ShipCrew)
from rest_framework.response import Response
# Create your views here.
from OAuth.serializers import *
from django.db.models import Q


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
class  UserViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','put']

    """
        List a queryset.
        """

    def list(self, request, *args, **kwargs):
        if request.user.roles == 1:
            self.queryset = self.queryset.filter(~Q(username='admin'))
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if request.user.roles == 1:
            return Response(status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        old_user = newuser.objects.get(id=request.user.id)
        user_info = self.perform_update(serializer)
        # user_info = self.perform_create(serializer)
        user_info.set_password(request.data['password'])
        headers = self.get_success_headers(serializer.data)
        user_info.save()

        try:
            # 如果船员
            if int(request.data['typevalue']) == 2:
                # 创建ship
                ship = Ship.objects.get(shipid=request.data['ShipID'])  # 获取对应的Ship对象
                ShipCrew.objects.get(user=user_info).ShipID = ship
        except:
            user_info.delete()
            old_user.save()
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def perform_update(self, serializer):
        return serializer.save()

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # if  newuser.objects.filter(email=request.data['email']).exists():
        #     return Response({'detail': '邮箱重复'}, status=status.HTTP_400_BAD_REQUEST)

        user_info = self.perform_create(serializer)
        user_info.set_password(request.data['password'])
        headers = self.get_success_headers(serializer.data)
        user_info.save()

        try:
            #如果船员
            if int(request.data['typevalue']) == 2:
                # 创建ship
                    ship = Ship.objects.get(shipid=request.data['ShipID'])  # 获取对应的Ship对象
                    ShipCrew.objects.create(user=user_info, ShipID=ship)
        except:
            user_info.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class UserDeleteViewSet(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['delete']
    # permission_classes = [] #后面再改

    def destroy(self, request, *args, **kwargs):
        if request.user.roles == 1:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class ShipCrewCreateViewSet(viewsets.ModelViewSet):
    queryset = ShipCrew.objects.all()
    serializer_class = ShipCrewSerializer
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

class ShipCrewCreateViewSet2(viewsets.ModelViewSet):
    queryset = newuser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        #创建ship
        try:
            ship = Ship.objects.get(shipid=request.data['ShipID'])  # 获取对应的Ship对象
            ShipCrew.objects.create(user=user, ShipID=ship)
        except:
            user.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

class ShipIDandNameViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    http_method_names = ['get']
    permission_classes = []

class ShipIDandNameAuthorViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    http_method_names = ['post','delete']
