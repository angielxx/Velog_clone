# Generated by Django 3.2.13 on 2022-09-16 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
