from django.shortcuts import render
import datetime
# Create your views here.

def about(request):
    return render(request, 'navigation/about.html')

def contact(request):
    return render(request, 'navigation/contact.html')
def home(request):
    d = {'author' : 'Rahim', 
         'age' : 25, 
         'lst' : ['python','is','best'], 
         'lst1' : ['legend'], 
         'birthday' : datetime.datetime.now(), 
         'val' : '' ,
         'lst2':[
               {'name': 'zed', 'age': 19},
               {'name': 'amy', 'age': 22},
               {'name': 'joe', 'age': 31},
               ],
         
    }
  
    return render(request, 'navigation/home.html',d)
