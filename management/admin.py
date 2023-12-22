from django.contrib import admin
from .models import Add

class AddModelAdmin(admin.ModelAdmin):  
    list_display = ("name",)

# Register your models here.
admin.site.register(Add, AddModelAdmin)