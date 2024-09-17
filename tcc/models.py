from django.db import models


class Register(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    date_of_birth = models.DateField()
    cell = models.CharField(max_length = 14)
    
    def __str__(self):
        return self.name
    
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