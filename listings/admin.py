from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','type','is_published','price','list_date','owner')
    list_display_links = ('id','title')
    list_filter = ('area','bedrooms','type')
    list_editable = ('is_published',)
    search_fields = ('title','type','price','address')
    list_per_page = 25


admin.site.register(Listing,ListingAdmin)

#./venv/Scripts/activate 