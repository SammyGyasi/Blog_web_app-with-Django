from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.home ,name='blog-home'),
    #views.home is the referring to the home function that we created
     path('about/' ,views.about ,name='blog-about'),
]
