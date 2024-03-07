from django.contrib import admin
from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('username','email','password','address','address2','city','state','zip_num','comments')
    
admin.site.register(Contact,ContactAdmin)
# Register your models here.
