from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, help_text='Blogger biography', blank=True)

    class Meta:
        verbose_name_plural = 'Bloggers'

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class Blog(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text='Blog title')
    content = models.TextField(max_length=3000, help_text='Blog content')
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def get_date(self):
        return f'{self.post_date.strftime("%b")} {self.post_date.day}, {self.post_date.year}'


class Comment(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, help_text='Enter the comment about the blog here')
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

    def get_date(self):
        return f'{self.post_date.strftime("%b")} {self.post_date.day}, {self.post_date.year}'
