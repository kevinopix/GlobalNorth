# Generated by Django 4.1.3 on 2023-05-20 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('Payment', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetail',
            name='customer_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.userprofile', verbose_name='Customer Email'),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.package', verbose_name='Package'),
        ),
    ]
