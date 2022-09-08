from django.db import models
# from taggit.managers import TaggableManager
# from django import forms


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # thumbnail = models.ImageField(upload_to='articles', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ssafyclass = models.CharField(max_length=10)
    # tags = TaggableManager()