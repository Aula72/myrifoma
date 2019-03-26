from django.urls import path, include
from myrifoma.views import *
app_name="myrifoma"
urlpatterns = [
    
    path('', index , name='index')
    
]