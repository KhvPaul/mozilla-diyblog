import datetime

from django.test import TestCase
from django.urls import reverse

from blog.forms import AddCommentModelForm

from django.contrib.auth.models import User

from blog.models import Blogger, Blog


class CreateBloggerFormTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username='tester')
        user.save()
        blogger = Blogger.objects.create(user=user)
        blogger.save()
        Blog.objects.create(author=blogger, title='Test title')

    def test_create_blogger_form_content_label(self):
        form = AddCommentModelForm()
        self.assertTrue(
            form.fields['content'].label is None or form.fields['content'].label == 'Your comment')

    def test_renew_form_content_field_help_text(self):
        form = AddCommentModelForm()
        self.assertEqual(form.fields['content'].help_text, 'Write your comment here')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('create-comment', kwargs={'pk': 1}))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))