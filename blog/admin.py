from django.contrib import admin
from blog.models import Post,Catgeory
# Register your models here.

@admin.register(Catgeory)
class CatgeoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    prepopulated_fields = {'slug':("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    prepopulated_fields = {'slug':("title",)}
