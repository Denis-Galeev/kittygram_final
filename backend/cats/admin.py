from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Achievement, Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'color',
        'birth_year',
        'owner',
        'image',
    )
    search_fields = ('name',)
    list_filter = ('birth_year',)
    list_display_links = ('name',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


admin.site.empty_value_display = '- пусто -'
admin.site.unregister(Group)
