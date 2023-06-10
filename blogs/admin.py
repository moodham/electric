from django.contrib import admin

# Register your models here.

from .models import posts,Article,comments,antena

admin.site.register(posts)
admin.site.register(Article)
admin.site.register(comments)
admin.site.register(antena)