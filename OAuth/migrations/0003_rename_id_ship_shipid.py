# Generated by Django 3.2.15 on 2024-06-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OAuth', '0002_analysisorganization_dataanalyst_port_regulatory_ship_shipcrew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ship',
            old_name='id',
            new_name='shipid',
        ),
    ]
