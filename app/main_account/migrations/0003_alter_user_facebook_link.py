# Generated by Django 3.2.5 on 2021-07-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0002_auto_20210717_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک فیس بوک'),
        ),
    ]
