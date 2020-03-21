from django import forms
from django.contrib.auth.models import User
from app.models import UserDataMod, Train

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password','email')
class UserDataForm(forms.ModelForm):
    class Meta():
        model=UserDataMod
        fields=('picture','user_site')
class TrainForm(forms.ModelForm):
    nickname=forms.ChoiceField(label='rrrr',choices=(('vv','VV'),('rr','RR')) )
    class Meta():
        model=Train
        fields=('user','nickname')
