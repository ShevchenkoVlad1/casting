# Generated by Django 2.0 on 2018-03-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0023_userip_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='ip',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]