# Generated by Django 2.0 on 2018-03-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0029_auto_20180318_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='images',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
