from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Post(models.Model):
     id = models.AutoField(primary_key=True)
     data_ora = models.DateTimeField(default=None)
     temp = models.IntegerField(default=None)
     hum = models.IntegerField(default=None)
     co2 = models.IntegerField(default=None)
     voc = models.IntegerField(default=None)
     pmio = models.IntegerField(default=None)
     pm25 = models.IntegerField(default=None)



     def __str__(self):
         return str(self.data_ora)