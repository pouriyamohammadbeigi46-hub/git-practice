from django.contrib import admin
from website.models import Contact
# Register your models here.

class Contactadmin (admin.ModelAdmin):


    date_hierarchy = "created_date"
    list_disaplay = ("name", "email", "created_date") 
    list_filter = ["email"]
    search_fields = ["name", "massage"]

admin.site.register(Contact,Contactadmin)

