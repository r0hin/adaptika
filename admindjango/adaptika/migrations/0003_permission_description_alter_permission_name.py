# Generated by Django 4.1 on 2022-08-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaptika', '0002_permission_remove_role_permissions_role_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
