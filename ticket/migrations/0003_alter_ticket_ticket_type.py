# Generated by Django 5.1.2 on 2024-11-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_contact_mode_ticket_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Compatibility Issue', 'Comaptibility Issue'), ('General', 'General')], default='General', max_length=20),
        ),
    ]