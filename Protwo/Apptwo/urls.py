from django.conf.urls import url
from Apptwo import views

app_name = 'Apptwo'

urlpatterns = [
    url("", views.users, name = "User"),
]
