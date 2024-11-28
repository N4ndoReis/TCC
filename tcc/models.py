from django.db import models
from django.core.validators import MinLengthValidator

class Register(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30, unique=True)
    #password = models.CharField(max_length = 128)
    date_of_birth = models.DateField()
    cell = models.CharField(max_length = 14)
    
    def __str__(self):
        return self.name
    
class Login(models.Model):
    email = models.EmailField(blank = False, max_length = 30,unique=True)
    password = models.CharField(max_length = 14)
    
    def __str__(self):
        return self.email
    
class Create(models.Model):
    PRIORITY = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
        
    )
    task = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100, blank = False)
    priority = models.CharField(max_length = 1, choices = PRIORITY, blank = False, null = False, default = 'B')
   
    def __str__(self):
        return self.task
    
class BringNote(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_in = models.DateTimeField(auto_now_add = True)
    updated_in = models.DateTimeField(auto_now = True)
   
    def __str__(self):
        return self.title
    
    
