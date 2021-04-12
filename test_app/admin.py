from django.contrib import admin

# Register your models here.
from django.forms import models

from test_app.models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    search_fields = 'name'.split()


class ProductAdmin(admin.ModelAdmin):
    fields = 'title description price category'.split()
    list_display = 'title description price category'.split()
    search_fields = 'title description'.split()

class ReviewAdmin(admin.ModelAdmin):
    list_display = 'text'.split()
    search_fields = 'text'.split()


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
