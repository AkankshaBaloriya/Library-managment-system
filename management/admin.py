from django.contrib import admin
from .models import Add, Student, IssuedBook

class AddModelAdmin(admin.ModelAdmin):  
    list_display = ["name", "price", "author", "quantity"]

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["name", "branch", "roll_no", "phone"]

class IssuedBookModelAdmin(admin.ModelAdmin):
    list_display = ["student_id", "isbn", "issued_date", "expiry_date"]


admin.site.register(Add, AddModelAdmin)
admin.site.register(Student, StudentModelAdmin)
admin.site.register(IssuedBook, IssuedBookModelAdmin)
