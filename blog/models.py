from django.db import models

# Create your models here.
class Catgeory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    options = (
        ("draft","draft"),
        ("published","published")
    )

    category = models.ForeignKey(Catgeory,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="cover_image")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=options,default="draft")

    class Meta:
        ordering =("-created_at",)

    def __str__(self):
        return self.title
