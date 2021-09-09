from django.contrib import admin

# Register your models here.
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','phone','contact_date')
    list_display_links = ('id','name')
    list_filter = ('contact_date',)
    search_fields = ('name','listing','email','phone','message')
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)