from django.contrib import admin
from .models import Manga, Chapter, Page

class PageInline(admin.TabularInline):
    model = Page
    extra = 1

class ChapterAdmin(admin.ModelAdmin):
    inlines = [PageInline]
    list_display = ['manga', 'number', 'title']
    ordering = ['manga', 'number']

class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

admin.site.register(Manga, MangaAdmin)
admin.site.register(Chapter, ChapterAdmin)
