from django.contrib import admin

# Register your models here.

from .models import Post, Category, Member,PostImage


admin.site.register(Category)
admin.site.register(Member)

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3
    fields = ('image','post')
    #extra is used to specify how many empty forms to show when creating a new post
    #fields is used to specify which fields to show in the inline forms

class PostAdmin(admin.ModelAdmin):
    list_filter = ('date', 'categories')
    search_fields = ('title', 'content')
    ordering = ('date','title')
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)