# Generated by Django 3.0.7 on 2020-09-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_remove_service_provider_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_provider',
            name='avg_rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
