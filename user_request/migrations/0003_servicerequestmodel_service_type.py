# Generated by Django 5.1 on 2024-08-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request', '0002_alter_servicerequestmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequestmodel',
            name='service_type',
            field=models.CharField(choices=[('maintainance', 'Maintainance'), ('refill', 'Refill'), ('leakage', 'Leakage'), ('exchange', 'Exchange'), ('payment', 'Payment'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
