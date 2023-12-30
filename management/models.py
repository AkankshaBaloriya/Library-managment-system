from django.db import models

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
    
    
class Issue_book(models.Model):
    student_name=models.CharField(max_length=50,default=None)
    student_id=models.IntegerField(default=0)
    branch=models.CharField(max_length=20, default=None)
    section=models.CharField(max_length=100, default=None)
    Book_name=models.CharField(max_length=100, default=None)
    Book_id=models.IntegerField(default=1) 
    quantity=models.IntegerField(default=1)    
    date_of_issue=models.DateField(("Date of Issue"), auto_now=False, auto_now_add=False)
    date_of_return=models.DateField(("Date of Return"), auto_now=False, auto_now_add=False)