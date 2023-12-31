# Generated by Django 2.2.28 on 2023-09-23 10:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('uid', models.PositiveIntegerField(unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('scheduled_status', models.CharField(choices=[('yet to scheduled', 'Yet to Scheduled'), ('scheduled', 'Scheduled')], max_length=25)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain_type', models.CharField(choices=[('event', 'Event'), ('others', 'Others')], max_length=6)),
                ('gain_coin', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercoin_created_user', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercoin_updated_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
