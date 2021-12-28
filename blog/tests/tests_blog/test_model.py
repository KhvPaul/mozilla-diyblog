import datetime

from django.test import TestCase

from blog.models import Blog, Blogger

from django.contrib.auth.models import User


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='tester', email='test@icloud.com', password='qwerty')
        author = Blogger.objects.create(user=user)
        Blog.objects.create(author=author, title='Some Title')

    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_content_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('content').max_length
        self.assertEqual(max_length, 3000)

    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.title}'
        self.assertEqual(str(blog), expected_object_name)

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), '/blog/1')

    def test_get_date(self):
        blog = Blog.objects.get(id=1)
        test_date = f'{datetime.datetime.now().strftime("%b")} {datetime.datetime.now().day}, {datetime.datetime.now().year}'
        self.assertEqual(blog.get_date(), test_date)
