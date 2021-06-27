from django.contrib import admin

from .models import News, Teachers, FeedBackViews, Table


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class TeachesAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'degree', 'rank', 'email')
    search_fields = ('full_name', 'degree', 'rank', 'email')


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc', 'created_at')
    search_fields = ('name', 'email', 'desc')


class TableAdmin(admin.ModelAdmin):
    list_display = ('table', 'created_at')
    list_display_links = ('created_at',)
    search_fields = ('created_at',)


admin.site.register(News, NewsAdmin)
admin.site.register(Teachers, TeachesAdmin)
admin.site.register(FeedBackViews, FeedBackAdmin)
admin.site.register(Table, TableAdmin)
