from django.contrib import admin
from comments.models import Category, Comment, UserProfile

class CategoryAdmin(admin.ModelAdmin):
  search_fields = ('name', )
  ordering = ('name',)

class CommentAdmin(admin.ModelAdmin):
  search_fields = ('body', )
  raw_id_fields = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)