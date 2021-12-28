from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Blog, Blogger


class BloggerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 blogs for pagination tests
        number_of_bloggers = 13
        for blogger_id in range(number_of_bloggers):
            user = User.objects.create(username=f'tester {blogger_id}',
                                       email='test@icloud.com',
                                       password='qwerty')
            author = Blogger.objects.create(user=user)
            Blog.objects.create(author=author, title=f'Some Title{blogger_id}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogger_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['blogger_list']), 5)

    def test_lists_all_blogs(self):
        response = self.client.get(reverse('bloggers') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['blogger_list']), 3)


class BloggerDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username=f'tester',
                                   email='test@icloud.com',
                                   password='qwerty')
        Blogger.objects.create(user=user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogger/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogger-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogger-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogger_detail.html')