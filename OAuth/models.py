from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class newuser(AbstractUser):
    role_type=[
        [0, 'admin'],
        [1, 'user'],
    ]

    roles = models.IntegerField(verbose_name='角色',choices=role_type,default=1)
    UserID = models.AutoField('用户ID', primary_key=True)
    # Name = models.CharField('用户名字', max_length=30)
    # # Password = models.CharField('密码', max_length=30)
    # UserType = models.CharField('用户类型', max_length=20)
    # Gender = models.CharField('性别', max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    # Age = models.IntegerField('年龄')
    # Phone = models.CharField('电话', max_length=20)
    # IDNumber = models.CharField('身份信息', max_length=20)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass