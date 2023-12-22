from django.db import models

# Create your models here.
class Add(models.Model):
    name=models.CharField(max_length=50,default=None)
    price=models.IntegerField(default=0)
    author=models.CharField(max_length=20, default=None)
    description=models.TextField(max_length=100, default=None)
    image=models.ImageField(upload_to='books', default='default.jpg')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def showbook():
        allbooks=Add.objects.all()
        return allbooks
    
 
    
    