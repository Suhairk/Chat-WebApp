from datetime import datetime
from pyexpat import model
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50)
    
class Message(models.Model):
    message_text = models.CharField(max_length=1000 ,blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    user_name = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('date',)
    
class privateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message_text = models.CharField(max_length=1000, blank=True)
    date = models.DateField(default= datetime.now, blank=True )
    
    def __str__(self):
        return (self.message_text)

    class Meta:
        ordering = ('date',)
    

    
 
    
    