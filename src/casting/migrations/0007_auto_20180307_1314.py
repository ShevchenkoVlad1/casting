# Generated by Django 2.0 on 2018-03-07 11:14
auto_now_add=True
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0006_auto_20180307_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
