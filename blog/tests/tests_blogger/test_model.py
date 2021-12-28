import datetime

from django.test import TestCase

from blog.models import Blogger

from django.contrib.auth.models import User


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='tester', email='test@icloud.com', password='qwerty')
        Blogger.objects.create(user=user)

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_bio_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_user_username(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f'{blogger.user.username}'
        self.assertEqual(str(blogger), expected_object_name)

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')
