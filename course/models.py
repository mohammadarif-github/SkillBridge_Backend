from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    Title = models.CharField(max_length=30,unique=True)
    Instructor = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Features = models.TextField()
    Target = models.TextField()
    Duration = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.Title
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    problem = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contact Us'
        
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"Reviewer {self.user.username}; Course {self.course.Title}"
        


    

