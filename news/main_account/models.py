from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.templatetags.static import static
# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=250,blank=True,null=True,verbose_name='توضیحات')
    email = models.EmailField(unique=True,verbose_name='ایمیل')
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
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

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('registration/adminlte/img/avatar5.png')

class LogoLoginManager(models.Manager):
    def get_active_logo(self):
        return self.get(is_active=True)



class LogoLogin(models.Model):
    title = models.CharField(max_length = 150, verbose_name='عنوان')
    logopic = models.ImageField(upload_to = 'blog-images',verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    objects = LogoLoginManager()
    class Meta:
         verbose_name = 'عکس صفحه ورود و ثبت نام'
         verbose_name_plural = 'عکس های صفحه ورود و ثبت نام'
         ordering = ['-created']
    
    def __str__(self):
        return self.title

