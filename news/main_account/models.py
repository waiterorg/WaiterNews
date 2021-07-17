from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=250,blank=True,null=True,verbose_name='توضیحات')
    email = models.EmailField(unique=True,verbose_name='ایمیل')
    facebook_link = models.URLField(unique= True,max_length=150,blank=True,null=True,verbose_name='لینک فیس بوک')
    youtube_link = models.URLField(unique= True,max_length=150,blank=True,null=True,verbose_name='لینک یوتیوب')
    instagram_link = models.URLField(unique= True,max_length=150,blank=True,null=True,verbose_name='لینک اینستاگرام')
    pinterest_link = models.URLField(unique= True,max_length=150,blank=True,null=True,verbose_name='لینک پینترست')
    tweeter_link = models.URLField(unique= True,max_length=150,blank=True,null=True,verbose_name='لینک توییتر')
    website_link = models.URLField(unique= False,max_length=150,blank=True,null=True,verbose_name='لینک وبسایت')

    