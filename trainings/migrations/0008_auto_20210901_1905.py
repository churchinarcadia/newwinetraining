# Generated by Django 3.2.6 on 2021-09-01 19:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0005_auto_20210901_1905'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainings', '0007_alter_term_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisetype',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='exercisetype_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='exercisetype_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='code_after_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Embed Code After URL'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='code_before_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Embed Code Before URL'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='recordinglocation_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='location',
            field=models.CharField(max_length=30, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='recordinglocation_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='recordinglocation',
            name='url_identifier',
            field=models.CharField(max_length=100, verbose_name='URL Identifier'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='registration_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='exercisetypes',
            field=models.ManyToManyField(blank=True, related_name='registration_exercisetypes', to='trainings.ExerciseType', verbose_name='Exercise Types'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='registration_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='signature',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Signature'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='registration_terms', to='trainings.term', verbose_name='Term'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='registration_users', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='term',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='term',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='term_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='term',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='term',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='term_languages', to='languages.language', verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='term',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='term',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='term_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='term',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='term',
            name='term',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring')], max_length=10, verbose_name='Term'),
        ),
        migrations.AlterField(
            model_name='term',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2000, message='Please enter an appropriate year.'), django.core.validators.MaxValueValidator(2040, message='Please enter an appropriate year.')], verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='text',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='text_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='text',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='text',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='text',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='text_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='text',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='trainingmeeting_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='trainingmeeting_languages', to='languages.language', verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='trainingmeeting_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='recording_released_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='recordingreleased_user', to=settings.AUTH_USER_MODEL, verbose_name='Recording Released By'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='recording_released_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Recording Released'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='recording_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Recording URL'),
        ),
        migrations.AlterField(
            model_name='trainingmeeting',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='userexercise_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='exercisetypes',
            field=models.ManyToManyField(related_name='userexercise_exercisetypes', to='trainings.ExerciseType', verbose_name='Exercise Types'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='userexercise_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='Modifier'),
        ),
        migrations.AlterField(
            model_name='userexercise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='userexercise_users', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]