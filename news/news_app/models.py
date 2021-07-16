from django.db import models
from main_account.models import User
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.
class CategoryManager(models.Manager):
    
    def get_active_category(self):
        active = self.filter(status=True)
        return active

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=150, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='ادرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(default=0, verbose_name='پوزیشن')
    objects = CategoryManager()
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=[ 'parent__id','position']

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):

    def get_published_article(self):
        published = self.filter(status='p') 
        return published



class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d','چک نویس'), # draft
        ('p','منتشر شده'), #publish
        ('i','در حال بررسی'), #investigation
        ('b','برگشت داده شده'), #back

    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article', verbose_name='نویسنده')
    title = models.CharField(max_length = 150, verbose_name='عنوان')
    slug = models.SlugField(max_length= 150, unique = True , verbose_name='ادرس لینک')
    category = models.ManyToManyField(Category,related_name='articles',verbose_name='دسته بندی')
    description = models.TextField(verbose_name='توضیحات')
    thumpnail = models.ImageField(upload_to = 'blog-images',verbose_name='تصویر')
    publish = models.DateTimeField(default = timezone.now,verbose_name='منتشر شده')
    created = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True,verbose_name='بروز رسانی شده')
    status = models.CharField(max_length= 1,choices=STATUS_CHOICES,verbose_name='وضعیت')
    objects = ArticleManager()
    class Meta:
         verbose_name = 'مقاله'
         verbose_name_plural = 'مقالات'
         ordering = ['-publish']
    


    def category_to_str(self):
        return " ,".join([category.title for category in self.category.get_active_category()])
    category_to_str.short_description='دسته بندی'

    def thumpnail_tag(self):
        return format_html("<img src='{}' width=95 height=75 style='border-radius: 5px;'>".format(self.thumpnail.url))
    thumpnail_tag.short_description = 'عکس مقاله'