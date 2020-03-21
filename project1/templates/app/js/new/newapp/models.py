from django.db import models

# Create your models here.
class Position(models.Model):
    position=models.CharField(max_length=64, verbose_name='Position')
    def __str__(self):
        return self.position
class Person(models.Model):
    first_name=models.CharField(max_length=64, verbose_name='First name')
    last_name=models.CharField(max_length=64, verbose_name='Last name')
    email=models.CharField(max_length=64, verbose_name='E-mail')
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    def __str__(self):
        return (self.first_name+" "+self.last_name)
