# Generated by Django 3.2.15 on 2024-06-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OAuth', '0005_alter_newuser_typevalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='roles',
            field=models.PositiveSmallIntegerField(choices=[(0, 'admin'), (1, 'user')], default=1, verbose_name='角色'),
        ),
    ]
