import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Protwo.settings")

import django
django.setup()

import random
from faker import Faker
from Apptwo.models import User

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        f_name = fakegen.company()
        l_name = fakegen.company()
        email = fakegen.url()

        user = User.objects.get_or_create(first_name = f_name, last_name = l_name, email_ad = email)[0]

N = int(input("Enter the number of fake population:"))
print("Populating script!")
populate(N)
print("Populating completed!")
