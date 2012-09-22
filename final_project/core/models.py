from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'date')

admin.site.register(Post, PostAdmin)