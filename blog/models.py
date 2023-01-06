from django.db import models

# Create your models here.

class Post(models.Model):
    options = (
        ("draft","draft"),
        ("published","published")
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=options,default="draft")

    class Meta:
        ordering =("-created_at",)

    def __str__(self):
        return self.title
