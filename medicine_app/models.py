from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=200,unique=True)
    

# Create your models here.
class Hospitals(models.Model):
    city_name = models.ForeignKey(City,on_delete=models.CASCADE )
    #city_name = models.ForeignKey(City,on_delete=models.CASCADE ,to_field='city_name')
    #city_name = models.ForeignKey(City, default=None ,on_delete=models.CASCADE )
    city_hospital = models.CharField(max_length=200)
    hospital_number = models.CharField(max_length=200)

