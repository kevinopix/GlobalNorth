# Generated by Django 4.1.3 on 2023-06-26 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimony',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
    ]
