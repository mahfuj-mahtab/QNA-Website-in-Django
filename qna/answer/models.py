from django.db import models
from home.models import *
from questions.models import *
# Create your models here.
class Answer(models.Model):
    A_Id =models.IntegerField(primary_key =True)
    Q_answer= models.CharField(max_length = 30)
    dislike= models.IntegerField()
    like =models.IntegerField()
    U_ID = models.ForeignKey(OurUser,on_delete = models.CASCADE)
    Q_ID = models.ForeignKey(Questions,on_delete = models.CASCADE)
    

    

