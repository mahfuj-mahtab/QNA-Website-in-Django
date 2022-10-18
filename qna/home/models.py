from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class OurUser(models.Model):
    U_Id =models.IntegerField(primary_key =True)
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    password = models.TextField()
    Bio = models.TextField()
    Num_of_followers = models.IntegerField()
    Num_of_following = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)


