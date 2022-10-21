from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
  'author':'Samuel',
    'title':'Blog-Post 1',
    'content':'First Post Content',
    'date_posted':'October 20,2018'
    },

     {
    'author':'Kobina',
    'title':'Blog-Post 2',
    'content':'Second Post Content',
    'date_posted':'October 21,2018'
    }
  
]



def home(request):
    context ={
        'posts':posts
    }
    return  render(request,'blogs/home.html',context)

def about(request):
    return  render(request,'blogs/about.html',{'title':'About'})
