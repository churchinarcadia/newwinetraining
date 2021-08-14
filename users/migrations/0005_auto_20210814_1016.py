# Generated by Django 3.2 on 2021-08-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0004_auto_20210814_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_groups', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_userpermissions', to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='usertypes',
            field=models.ManyToManyField(blank=True, related_name='user_usertypes', to='users.UserType'),
        ),
    ]
