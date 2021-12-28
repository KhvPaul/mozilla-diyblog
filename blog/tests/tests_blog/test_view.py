from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Blog, Blogger


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 blogs for pagination tests
        number_of_blogs = 13
        for blog_id in range(number_of_blogs):
            user = User.objects.create(username=f'tester {blog_id}',
                                       email='test@icloud.com',
                                       password='qwerty')
            author = Blogger.objects.create(user=user)
            Blog.objects.create(author=author, title=f'Some Title{blog_id}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['blog_list']), 5)

    def test_lists_all_blogs(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blogs') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['blog_list']), 3)


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username=f'tester',
                                   email='test@icloud.com',
                                   password='qwerty')
        author = Blogger.objects.create(user=user)
        Blog.objects.create(author=author, title=f'Some Title')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
