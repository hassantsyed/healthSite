from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    experience = models.TextField(max_length=300)
    location = models.TextField(max_length=100)
    EXPERTISE = (('NUTRITION','Nutritionist'), ('TRAIN', 'Personal Trainer'), ('MD', 'Doctor'), ('User', 'User'))
    area = models.CharField(max_length=15, choices=EXPERTISE, default='User')
    group = models.ManyToManyField('self')
    pic = models.ImageField(upload_to='media/', default='media/noprofile.png')
