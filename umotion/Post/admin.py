from django.contrib import admin
from Post.models import Post
from Post.models import Comment

admin.site.register(Post)
admin.site.register(Comment)
