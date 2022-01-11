from django.contrib import admin
from .models import Photo, Category
# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "category",
        "image",
        "description",
        "add_date",
    ]

admin.site.register(Category)
