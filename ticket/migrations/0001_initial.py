# Generated by Django 5.1.2 on 2024-11-01 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=15, unique=True)),
                ('ticket_title', models.CharField(max_length=50)),
                ('ticket_description', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='engineer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]