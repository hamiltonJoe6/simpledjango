# Generated by Django 4.1.2 on 2022-10-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0003_stu_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
