# Generated by Django 5.1 on 2024-08-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequestmodel',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('addressed', 'Addressed')], default='pending', max_length=20),
        ),
    ]
