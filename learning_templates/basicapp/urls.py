from django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    url('other/', views.other, name='other'),
    url('relative/', views.relative, name='relative'),
]
