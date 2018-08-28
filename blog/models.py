from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 255)
    posted_on = models.DateTimeField(auto_now_add = True)
    edited_on = modes.DateTimeField(auto_now = True)
    Content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name = "blog_posts")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-posted_on', 'title']

class Tag(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
