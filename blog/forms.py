from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Comment


class AddCommentModelForm(ModelForm):
    def clean_content(self):
        content = self.cleaned_data['content']
        return content

    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Your comment', }
        help_texts = {'content': 'Write your comment here', }


class CreateBloggerForm(forms.Form):
    username = forms.CharField(max_length=30, label='username', help_text='Your username')
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=50, help_text='Your password')
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=50, help_text='Confirm your password')
    email = forms.EmailField(label='email', help_text='Your email')
    bio = forms.CharField(max_length=3000, widget=forms.Textarea, required=False, help_text='Your biography')

    # class Meta:
    #     fields = ['username', 'password1', 'password2', 'email', 'bio']
    #     labels = {'username': 'Your username',
    #               'password1': 'password',
    #               'password2': 'password confirm',
    #               'email': 'email field',
    #               'bio': 'some info about you'}
    #     help_texts = {'username': 'Your username',
    #                   'password1': 'password',
    #                   'password2': 'password confirm',
    #                   'email': 'email field',
    #                   'bio': 'some info about you'}

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            raise forms.ValidationError("This username already exists")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError("Please enter the password")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("Please confirm the password")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.endswith("@test.com"):
            raise forms.ValidationError("Email can't ends with 'test.com'")
        return email

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        # if not bio or bio != '':
        #     raise forms.ValidationError("Please enter your biography")
        return bio

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
