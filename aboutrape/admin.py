from django.contrib import admin
from aboutrape.models import Category, Comment

class CategoryAdmin(admin.ModelAdmin):
  search_fields = ('__unicode__', 'name',)
  ordering = ('name',)

class CommentAdmin(admin.ModelAdmin):
  search_fields = ('body', )
  raw_id_fields = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)