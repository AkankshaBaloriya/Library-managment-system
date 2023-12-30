from django.contrib import admin
from .models import Add,Issue_book

class AddModelAdmin(admin.ModelAdmin):  
    list_display = ("name",)

class Adminissuebook(admin.ModelAdmin):
    list_display=('student_name',)

# Register your models here.
admin.site.register(Add, AddModelAdmin)
admin.site.register(Issue_book,Adminissuebook)