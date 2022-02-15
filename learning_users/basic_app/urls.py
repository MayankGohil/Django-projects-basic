from django.conf.urls import url 
from basic_app import views 

urlpatterns = [
    url('user_login/', views.user_login, name='user_login'),
]
