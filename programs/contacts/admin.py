from django.contrib import admin
from contacts.models import Contacts
# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_firstname','contact_lastname','contact_email','contact_mobilenumber','contact_message')
admin.site.register(Contacts,ContactsAdmin)

