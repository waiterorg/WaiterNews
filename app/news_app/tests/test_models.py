from django.test import TestCase
from ..models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.category = Category.objects.create(title='django', slug='django', status='False')



    def test_title_label(self):
        """
        test title vernose name
        """
        field_label = self.category._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'عنوان دسته بندی')
    
    def test_slug_label(self):
        """
         test slug vernose name 
        """
        field_label = self.category._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'ادرس دسته بندی')


    def test_title_max_length(self):
        """
         test title max length 
        """
        max_length = self.category._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.category
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_manager_get_active_category(self):
        category = Category.objects.get_active_category()
        self.assertEqual(category.count(), 0)

    def test_default_position(self):
        position = self.category.position
        self.assertEqual(position,0)