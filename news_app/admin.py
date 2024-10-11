from django.contrib import admin
from .models import Category, News, Contact, ContactData

# Register your models here.

#1
# admin.site.register(Category)
# admin.site.register(News)
admin.site.register(Contact)

#2

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


admin.site.register(ContactData)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'active_comments']

    def disable_comments(self, request, queryset):
        queryset.updata(active=False)

    def active_comments(self, request, queryset):
        queryset.updata(active=True)

