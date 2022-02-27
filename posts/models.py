from django.utils.text import slugify
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
