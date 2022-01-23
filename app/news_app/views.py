import json
from datetime import timedelta, datetime
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery.schedules import crontab
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.contrib import messages
from main_account.models import User
from .models import Article, Category


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.get_published_article()
    paginate_by = 8
    


class ArticleDetail(DetailView):

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = Article.objects.get_published_article()
        article = get_object_or_404(article, slug=slug)

        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article

class CategoryList(ListView):
    paginate_by = 8
    template_name = 'news_app/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(
            Category.objects.get_active_category(), slug=slug)
        return category.articles.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class AuthorList(ListView):
    paginate_by = 8
    template_name = 'news_app/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.article.get_published_article()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context

@login_required
def mail_weekely_articles(request):
    try:
        last_week = timezone.now() - timedelta(days=7)
        last_week_articles = Article.objects.filter(publish__gte=last_week, status='p')[:10]
        subject = 'مقالات جدید این هفته'
        current_site = get_current_site(request)
        message = render_to_string('registration/weekely_articles_email.html', {
                'articles': last_week_articles,
                'user': request.user,
                'domain': current_site.domain,
            })
        current_time = datetime.now()
        # for diffrence number of days of week between  crontab and datetime , give 1 day to current time to eqauls with crontab days of week number
        # for example in datetime sunday is 6 but in crontab sunday is 0 so in datetime 6 + 1 = 0 for weekday
        exchange_number_day_of_week = current_time + timedelta(days=1)
        current_day_of_week = exchange_number_day_of_week.weekday()
        schedule, created = CrontabSchedule.objects.get_or_create(hour = current_time.hour, minute = current_time.minute, day_of_week = current_day_of_week)
        task = PeriodicTask.objects.create(crontab=schedule, name=f"weekely_mail_task_{request.user.pk}", 
                                           task='main_account.tasks.send_mail_from_webmaster_task', 
                                           args = json.dumps([subject, message, [request.user.email]]))
        messages.success(request, "در خواست شما با موفقیت ثبت گردید !")
        return redirect('/')
    except ValidationError:
        messages.warning(request, "شما یک بار درخواست داده اید !")
        return redirect("/")