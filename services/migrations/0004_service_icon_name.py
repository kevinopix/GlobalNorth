# Generated by Django 4.1.3 on 2023-06-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
