import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_First.settings")

import django
django.setup()

import random
from First_App.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Sports', 'Social', 'MarketPlace', 'Games', 'News']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=3):

    for entry in range(N):

        top = add_topic()

        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]

        accrecord = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

N = int(input("Enter the number of fake population:"))
print("Populating script!")
populate(N)
print("Populating completed!")
