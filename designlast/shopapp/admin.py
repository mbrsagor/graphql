from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Slider)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Category)


class PorductModel(admin.ModelAdmin):
    list_display    = ['name', 'category', 'color', 'brand_name', 'publish_on', 'update_on']
    date_hierarchy  = 'publish_on'
    list_per_page   = 15
admin.site.register(Product, PorductModel)
