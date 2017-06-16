from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        abstract=True
    
    user = models.OneToOneField(User)
    myuniv = models.CharField(max_length=30, blank=True)