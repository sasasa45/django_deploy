import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','new.settings')

import django
# Import settings
django.setup()

import random
from newapp.models import Person, Position
from faker import Faker
sett=['docent','assistant','professor','student','aspirant']
f=Faker()
def make_position():
    pos=Position.objects.get_or_create(position=random.choice(sett))[0]
    pos.save()
    return pos
def make_person(n=10):
    for i in range(n):
        pos=make_position()
        faker_first_name=f.first_name()
        faker_last_name=f.last_name()
        faker_emial=f.email()
        person=Person.objects.get_or_create(first_name=faker_first_name,last_name=faker_last_name,email=faker_emial,position=pos)[0]
if __name__=='__main__':
    make_person(n=15)
