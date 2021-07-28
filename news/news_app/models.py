from django.db import models
from main_account.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from datetime import datetime, timedelta
from django.db.models import Q, Count
from star_ratings.models import Rating

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

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")    


class ArticleManager(models.Manager):

    def get_published_article(self):
        published = self.filter(status='p') 
        return published
    
    def get_popular_articles(self):
        last_month = datetime.today() - timedelta(days=30)
        popular_articles = self.get_published_article().annotate(count=Count('hits', filter=Q(articlehit__created__gte=last_month))).order_by('-count', '-publish')[:5]
        return popular_articles

    def get_top_rated_articles(self):
        last_month = datetime.today() - timedelta(days=30)
        top_rated = self.filter(created__gte=last_month, ratings__isnull=False).order_by('-ratings__average', '-publish')[:5]
        return top_rated

    def get_hot_articles(self):
        last_month = datetime.today() - timedelta(days=30)
        hot_article = self.get_published_article().annotate(count=Count('comments', filter=Q(comments__posted__gte=last_month) and Q(comments__content_type_id=8))).order_by('-count', '-publish')[:5]
        return hot_article
  

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
    is_special = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name="hits", verbose_name="بازدید ها")
    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating, related_query_name='ArticleRating')
    objects = ArticleManager()
    class Meta:
         verbose_name = 'مقاله'
         verbose_name_plural = 'مقالات'
         ordering = ['-publish']
    
    def __str__(self):
        return self.title

    def category_to_str(self):
        return " ,".join([category.title for category in self.category.get_active_category()])
    category_to_str.short_description='دسته بندی'

    def get_absolute_url(self):
        return reverse("account:home")

    def thumpnail_tag(self):
        return format_html("<img src='{}' width=95 height=75 style='border-radius: 5px;'>".format(self.thumpnail.url))
    thumpnail_tag.short_description = 'عکس مقاله'



class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
