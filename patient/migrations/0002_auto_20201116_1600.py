# Generated by Django 3.1.3 on 2020-11-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='deceased',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
