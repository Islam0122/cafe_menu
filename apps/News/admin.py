from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'content')
    list_filter = ('pub_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Медиа', {
            'fields': ('image',),
        }),
        ('Информация о дате', {
            'fields': ('pub_date',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('pub_date',)


admin.site.register(News, NewsAdmin)
