from django.contrib import admin
from .models import Post, Comment, Categories, TagModel

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(TagModel)