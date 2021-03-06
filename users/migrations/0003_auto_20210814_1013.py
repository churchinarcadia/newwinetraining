# Generated by Django 3.2 on 2021-08-14 10:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_initial'),
        ('users', '0002_auto_20210814_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('B', 'Brother'), ('S', 'Sister')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_languages', to='languages.language', verbose_name='Primary Language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='locality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_localities', to='users.locality'),
        ),
        migrations.AlterField(
            model_name='user',
            name='modifier',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='user_modifiers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None, validators=[django.core.validators.RegexValidator(message='Please enter your 10-digit phone number (including area code) without dashes or anything else.', regex='^[(]?[2-9]\\d{2}[) -.]{0,2}\\d{3}[ -.]?\\d{4}$')]),
        ),
    ]
