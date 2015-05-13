from django.contrib import admin
from aboutrape.models import Category, Comment

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('__unicode__', 'name',)
  search_fields = ('name', )
  ordering = ('name',)

class CommentAdmin(admin.ModelAdmin):
  list_display = ('__unicode__', 'body',)
  search_fields = ('body', )
  raw_id_fields = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)