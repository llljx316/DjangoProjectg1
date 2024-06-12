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

class Ship(models.Model):
    shipid = models.AutoField(primary_key=True)  # 船只ID
    name = models.CharField(max_length=100, db_index=True)  # 船只名称
    ship_type = models.CharField(max_length=50)  # 船只类型
    capacity = models.FloatField()  # 船只载重量
    length = models.FloatField()  # 船只长度
    width = models.FloatField()  # 船只宽度
    height = models.FloatField()  # 船只高度
    draft = models.FloatField()  # 船只吃水
    status = models.CharField(max_length=50)  # 船只状态
    country = models.CharField(max_length=50)  # 船只所属国家

    # def __str__(self):
    #     return self.name


class newuser(AbstractUser):
    # role_type=[
    #     [0, 'admin'],
    #     [1, 'user'],
    # ]
    role_type = (
        (0, 'admin'),
        (1, 'user'),
    )

    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'shipcrew'),
        (3, 'analyst'),
        (4, 'supervisor')
    )

    typevalue = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    is_type1 = models.BooleanField(default=False)

    roles = models.PositiveSmallIntegerField(verbose_name='角色',choices=role_type,default=1)
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



class DataAnalyst(models.Model):
    user = models.OneToOneField(newuser, on_delete=models.CASCADE, primary_key=True)
    AppointerID = models.ForeignKey(AnalysisOrganization, on_delete=models.SET_NULL, null=True)

class ShipCrew(models.Model):
    user = models.OneToOneField(newuser, on_delete=models.CASCADE, primary_key=True)
    ShipID = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True)