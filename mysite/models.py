from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class PersonalDetails(models.Model):
    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    hobbies = ArrayField(ArrayField(models.CharField(max_length=100)))
