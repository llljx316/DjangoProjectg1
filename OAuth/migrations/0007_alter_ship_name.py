# Generated by Django 3.2.15 on 2024-06-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OAuth', '0006_alter_newuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
