from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
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

    is_author = models.BooleanField(default=False,verbose_name="وضعیت نویسنده")
    special_user = models.DateTimeField(default = timezone.now,verbose_name='کاربر ویژه تا ')

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.short_description = 'کاربر ویژه'
    is_special_user.boolean = True

    