from django.contrib import admin
from .models import Comment, Post, Department

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Department)
