# Generated by Django 4.0 on 2021-12-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='bio',
            field=models.TextField(help_text='Blogger biography', max_length=1000, null=True),
        ),
    ]
