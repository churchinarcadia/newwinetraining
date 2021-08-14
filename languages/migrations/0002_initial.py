# Generated by Django 3.2 on 2021-08-13 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='translation_creators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='translation',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='translation_languages', to='languages.language'),
        ),
        migrations.AddField(
            model_name='translation',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='translation_modifiers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='translation',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_texts', to='trainings.text'),
        ),
        migrations.AddField(
            model_name='language',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='language_creators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='language',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='language_modifiers', to=settings.AUTH_USER_MODEL),
        ),
    ]