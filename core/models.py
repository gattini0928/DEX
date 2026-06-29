from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(blank=False, null=False, max_length=20)

    def __str__(self):
        return self.name

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True)
    query = models.CharField(max_length=255)
    what_is = models.TextField()
    how_it_works = models.TextField()
    code_example = models.TextField()
    when_to_use = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.query)
        super().save(*args, **kwargs)
