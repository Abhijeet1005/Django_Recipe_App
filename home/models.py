from django.db import models

class Student(models.Model):

    # id = models.AutoField() This gets auto created by django and is also the primary key
    name = models.CharField(max_length=50)
    age =  models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null= True)
    image =  models.ImageField()
    file =  models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_speed = models.IntegerField(default=60)

    def __str__(self) -> str:
        return str(self.car_name + str(self.car_speed))