# Generated by Django 3.2.5 on 2021-07-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک فیس بوک'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='pinterest_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک پینترست'),
        ),
        migrations.AddField(
            model_name='user',
            name='tweeter_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک توییتر'),
        ),
        migrations.AddField(
            model_name='user',
            name='website_link',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='لینک وبسایت'),
        ),
        migrations.AddField(
            model_name='user',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='لینک یوتیوب'),
        ),
    ]