from django.contrib import admin

# Register your models here.
from .models import Owner
# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    list_filter = ('hire_date',)
    search_fields = ('name',)

    list_per_page = 25


admin.site.register(Owner,OwnerAdmin)