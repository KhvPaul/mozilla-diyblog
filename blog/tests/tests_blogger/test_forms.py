from django.test import TestCase

from blog.forms import CreateBloggerForm

from django.contrib.auth.models import User

from blog.models import Blogger


class CreateBloggerFormTest(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(username='tester')
        user.save()
        Blogger.objects.create(user=user, bio='Some info')

    def test_create_blogger_form_username_field_label(self):
        form = CreateBloggerForm()
        self.assertTrue(
            form.fields['username'].label is None or form.fields['username'].label == 'username')

    def test_create_blogger_form_password1_field_label(self):
        form = CreateBloggerForm()
        self.assertTrue(
            form.fields['password1'].label is None or form.fields['password1'].label == 'password1')

    def test_create_blogger_form_password2_field_label(self):
        form = CreateBloggerForm()
        self.assertTrue(
            form.fields['password2'].label is None or form.fields['password2'].label == 'password2')

    def test_create_blogger_form_email_field_label(self):
        form = CreateBloggerForm()
        self.assertTrue(
            form.fields['email'].label is None or form.fields['email'].label == 'email')

    def test_create_blogger_form_bio_field_label(self):
        form = CreateBloggerForm()
        self.assertTrue(
            form.fields['bio'].label is None or form.fields['bio'].label == 'bio')

    def test_renew_form_username_field_help_text(self):
        form = CreateBloggerForm()
        self.assertEqual(form.fields['username'].help_text, 'Your username')

    def test_renew_form_password1_field_help_text(self):
        form = CreateBloggerForm()
        self.assertEqual(form.fields['password1'].help_text, 'Your password')

    def test_renew_form_password2_field_help_text(self):
        form = CreateBloggerForm()
        self.assertEqual(form.fields['password2'].help_text, 'Confirm your password')

    def test_renew_form_email_field_help_text(self):
        form = CreateBloggerForm()
        self.assertEqual(form.fields['email'].help_text, 'Your email')

    def test_renew_form_bio_field_help_text(self):
        form = CreateBloggerForm()
        self.assertEqual(form.fields['bio'].help_text, 'Your biography')

    def test_renew_form_username_exists(self):
        # User.objects.create(username='test_username')
        form = CreateBloggerForm(data={'username': 'tester',
                                       'password1': 'qwerty123',
                                       'password2': 'qwerty123',
                                       'email': 'email@mail.com'})
        self.assertFalse(form.is_valid())

    def test_renew_form_wrong_email(self):
        form = CreateBloggerForm(data={'username': 'test_username',
                                       'password1': 'qwerty123',
                                       'password2': 'qwerty123',
                                       'email': 'email@test.com'})
        self.assertFalse(form.is_valid())

    def test_renew_form_passwords_didnt_match(self):
        form = CreateBloggerForm(data={'username': 'test_username',
                                       'password1': 'qwerty123',
                                       'password2': 'wrong_password',
                                       'email': 'email@test.com'})
        self.assertFalse(form.is_valid())

    def test_renew_form_passwords_match(self):
        form = CreateBloggerForm(data={'username': 'test_username',
                                       'password1': 'qwerty123',
                                       'password2': 'qwerty123',
                                       'email': 'email@test.com'})
        self.assertFalse(form.is_valid())
