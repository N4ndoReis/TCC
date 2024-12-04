from django.db import models
from django.core.validators import MinLengthValidator
from tcc.validators import invalid_name, invalid_cell

class Register(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[invalid_name],  
    )
    email = models.EmailField(
        blank=False,
        max_length=254,  
        unique=True
    )
    password = models.CharField(
        max_length=128
    )
    date_of_birth = models.DateField()
    cell = models.CharField(
        max_length=14,
        validators=[invalid_cell] 
    )
    
    def __str__(self):
        return self.name
    
class Login(models.Model):
    email = models.EmailField(
        blank=False,
        max_length=254,
        unique=True
    )
    password = models.CharField(
        max_length=128
    )
    
    def __str__(self):
        return self.email
    
class Create(models.Model):
    PRIORITY = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
    )
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY,
        blank=False,
        null=False,
        default='B'
    )
   
    def __str__(self):
        return self.task

    
class BringNote(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
    
    
