from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDataMod(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    picture=models.ImageField(null=True,blank=True,upload_to='app')
    user_site=models.URLField(blank=True,null=True)
    def __str__(self):
        return self.user.username
class  Train(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=256)
    def __str__(self):
        return self.nickname
