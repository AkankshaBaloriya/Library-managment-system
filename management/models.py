from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Add(models.Model):
    name=models.CharField(max_length=50,default=None)
    price=models.IntegerField(default=0)
    author=models.CharField(max_length=20, default=None)
    description=models.TextField(max_length=100, default=None)
    image=models.ImageField(upload_to='books', default='default.jpg')
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def showbook():
        allbooks=Add.objects.all()
        return allbooks
    
    @staticmethod
    def book_detail(id):
        return Add.objects.get(id=id)   

class Student(models.Model):
    name = models.CharField(max_length=16)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
 
    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'
 
def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)   
    