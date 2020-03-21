from django import forms
from django.core import validators
from newapp.models import Person
# def zi(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("not z")
class Users(forms.ModelForm):
    # name=forms.CharField(  )
    # same_name=forms.CharField( )
    # email=forms.EmailField()
    class Meta():
        model=Person
        fields='__all__'

    # def clean(self):
    #     common=super().clean()
    #     if common['name']!=common['same_name']:
    #         raise forms.ValidationError("not equal")
