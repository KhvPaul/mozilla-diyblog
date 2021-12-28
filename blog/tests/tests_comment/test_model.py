import datetime

from django.test import TestCase

from blog.models import Blog, Blogger, Comment

from django.contrib.auth.models import User


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='tester', email='test@icloud.com', password='qwerty')
        author = Blogger.objects.create(user=user)
        blog = Blog.objects.create(title='Test blog', author=author)
        Comment.objects.create(author=author, content='test content', blog=blog)

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_content_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_content_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('content').max_length
        self.assertEqual(max_length, 1000)

    def test_get_date(self):
        comment = Comment.objects.get(id=1)
        test_date = f'{datetime.datetime.now().strftime("%b")} {datetime.datetime.now().day}, {datetime.datetime.now().year}'
        self.assertEqual(comment.get_date(), test_date)

    def test_object_name_is_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.content}'
        self.assertEqual(str(comment), expected_object_name)
