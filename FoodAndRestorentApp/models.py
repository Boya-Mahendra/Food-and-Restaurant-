from django.db import models

# Create your models here.
class Food(models.Model):
    Fid=models.IntegerField(primary_key=True)
    FoodName=models.CharField(max_length=50)
    FoodPrice=models.IntegerField()




class Restorent(models.Model):
    RId=models.IntegerField(primary_key=True)
    RName=models.CharField(max_length=50)
    RLocation=models.TextField(max_length=120)