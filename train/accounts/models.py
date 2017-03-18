from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class User(AbstractUser):
    experience = models.TextField(max_length=300)
    state = models.TextField(max_length=100, default="")
    city = models.TextField(max_length=100, default="")
    EXPERTISE = (('NUTRITION','Nutritionist'), ('TRAIN', 'Personal Trainer'), ('MD', 'Doctor'), ('User', 'User'))
    area = models.CharField(max_length=15, choices=EXPERTISE, default='User')
    group = models.ManyToManyField('self', blank=True)
    pic = models.ImageField(upload_to='media/', default='media/noprofile.png')

class Weight(models.Model):
    pds = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    person = models.ForeignKey(User)
