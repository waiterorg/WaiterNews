from django.urls import reverse
from django.test import TestCase
from django.http import HttpRequest
from django.test.client import Client, RequestFactory
from main_account.models import User
from ..models import Category, Article
from ..views import ArticleListView

class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        user = User.objects.create(username='admin',password='helloo',email='test@ex.to')
        category = Category.objects.create(title='django', slug='django')
        article = Article.objects.create(title='django beginners', description='django beginners',
                               slug='django-beginners', thumpnail='django', status='p',author=user,created='2021-07-19 17:21:32.541294+04:30',
                               updated='2021-07-19 17:21:32.541294+04:30',
                               publish='2021-07-19 17:21:32.541294+04:30')
        article.category.add(category)
    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url(self):
        """
        Test articles response status
        """
        response = self.c.get(
            reverse('news:articledetail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """
        Test articles for each category response status
        """
        response = self.c.get(
            reverse('news:CategoryView', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = self.factory.get('/')
        response = ArticleListView.as_view()(request)
        rendered_response = response.render()
        html = rendered_response.content.decode('utf8')
        self.assertTrue(html.startswith('\n\n<!DOCTYPE html>'))
        self.assertEqual(response.status_code, 200)