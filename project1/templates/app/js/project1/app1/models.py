from django.db import models

# Create your models here.
class Topic(models.Model):
    main_topic=models.CharField(max_length=64)
    def __str__(self):
        return self.main_topic
class People(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=64, unique=True)
    url=models.URLField(unique=True)
    def __str__(self):
        return self.url
class Date(models.Model):
    namme=models.ForeignKey(People,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
