from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Port(models.Model):
    PortID = models.AutoField('港口ID',primary_key=True)
    Name = models.CharField('港口的名称',max_length=50)
    Location = models.CharField('位置',max_length=100)
    Type = models.CharField('港口的类型',max_length=30)
    Capacity = models.IntegerField('港口的容量')


class Organization(models.Model):
    # OrganizationID = models.AutoField('机构ID',primary_key=True)
    Name = models.CharField('机构名字',max_length=50)
    Address = models.CharField('机构地址',max_length=100)
    Phone = models.CharField('机构电话',max_length=20)
    class Meta:
        abstract = True

class Regulatory(Organization):
    RegulatoryID = models.AutoField('监管局ID',primary_key=True)

class AnalysisOrganization(Organization):
    AnalysisID = models.AutoField('分析机构ID',primary_key=True)



class newuser(AbstractUser):
    role_type=[
        [0, 'admin'],
        [1, 'user'],
    ]

    is_type1 = models.BooleanField(default=False)

    roles = models.IntegerField(verbose_name='角色',choices=role_type,default=1)
    id = models.AutoField('用户ID', primary_key=True)
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

# class UserPortAdmin(models.Model):
#     user = models.OneToOneField(newuser, on_delete=models.CASCADE, primary_key=True)
#