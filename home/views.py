from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

peoples = [
    {'name': 'asc', 'age': 21},
    {'name': 'abc', 'age': 22},
    {'name': 'xyz', 'age': 27},
           ]

text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
games = ["Witcher","Spiderman","Rdr2","God of war"]


def home(request):
    
    return render(request, 'home/index.html',context= {'peoples' : peoples,'text':text,'games':games,'page': 'Homepage'})

def about(request):
    context = {'page': 'About'}
    return render(request, 'home/about.html',context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, 'home/contact.html',context)