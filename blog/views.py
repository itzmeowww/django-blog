from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'ItzMeOwww',
        'title':'My First Blog',
        'content': 'This is my first blog',
        'date_posted':'August 27, 2020',
    },
    {
        'author':'Thanasan Kumdee',
        'title':'First Blog ',
        'content': 'This is my first blog on this site',
        'date_posted':'August 29, 2020',
    }
]

def home(request) :
    context = {
        'posts':posts,
        'css':'home.css'
    }
    return render(request,'blog/home.html',context)

def about(request) :
    return render(request,'blog/about.html',{'css':'about.css','title':'About'})
