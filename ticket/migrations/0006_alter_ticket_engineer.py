# Generated by Django 5.1.2 on 2024-11-03 04:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_alter_ticket_contact_mode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='engineer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='engineer', to=settings.AUTH_USER_MODEL),
        ),
    ]
