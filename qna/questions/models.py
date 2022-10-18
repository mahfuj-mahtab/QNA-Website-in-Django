from django.db import models
from home.models import *
# Create your models here.
class Questions(models.Model):
    Q_Id =models.IntegerField(primary_key =True)
    title = models.CharField(max_length = 30)
    details = models.CharField(max_length = 50)
    U_ID = models.ForeignKey(OurUser,on_delete = models.CASCADE)
    cat_name = models.CharField(max_length = 50)
    
