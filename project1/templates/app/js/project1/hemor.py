import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
# Import settings
django.setup()
import random
from app1.models import Topic, People,Date
from faker import Faker

faker=Faker()
Totopics=['Search','Social','Marketplace','News','Games']

def top():
    t=Topic.objects.get_or_create(main_topic=random.choice(Totopics))[0]
    t.save()
    return t
def collaps(n=5):
    for i in range(n):
        topp=top()

        fake_name=faker.company()
        fake_url=faker.url()
        fake_date=faker.date()
        ppl=People.objects.get_or_create(name=fake_name,url=fake_url,topic=topp)[0]
        dt=Date.objects.get_or_create(date=fake_date,namme=ppl)[0]



if __name__=="__main__":
    collaps(n=10)
    print(faker.timezone())
