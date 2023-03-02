from django.contrib import admin

from stu.models import Stu, Comment, Post

class StuModel(admin.ModelAdmin):
	list_display = ['title', 'content']
	list_display_links = ['title', 'content']
	search_fields = ['title']

admin.site.register(Stu, StuModel)
admin.site.register(Comment)
admin.site.register(Post)
