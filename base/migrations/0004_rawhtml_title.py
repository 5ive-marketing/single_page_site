# Generated by Django 2.2.6 on 2019-12-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rawhtml'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawhtml',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
