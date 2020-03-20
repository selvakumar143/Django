from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

def ListPerson(request):
     data = Person.objects.all()
     return render(request,'persons/list.html',{'persons':data})
def CreatePerson(request):
     form = PersonForm(request.POST or None)
     if form.is_valid():
          form.save()
          return redirect('/person/')
     return render(request,'persons/create.html',{'form':form})

def UpdatePerson(request,id):
     person=Person.objects.get(id=id)
     form = PersonForm(request.POST or None,instance=person)

     if form.is_valid():
          form.save()
          return redirect('/person/')

     return render(request,'persons/create.html',{'form':form,'person':person})

def DeletePerson(request,id):
     person=Person.objects.get(id=id)
     if request.method=="POST":
          person.delete()
          return redirect('/person/')
     return render(request,'persons/person-delete-confirm.html',{'person':person})
