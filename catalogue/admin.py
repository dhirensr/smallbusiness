from django.contrib import admin

from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created", "updated", "url"]
    list_filter = ["created", "updated", "category"]
    list_editable = []
    save_as = True


admin.site.register(Page, PageAdmin)
