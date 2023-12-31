from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
     # messages.success(request,"This is a test message")
     return render(request,'index.html',{'variable':2,'variable1':3})

def about(request):
     return render(request,'about.html')
def services(request):
     return render(request,'services.html')
def contact(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          try:
               contact= Contact(name=name,email=email,phone=phone,desc=desc,create_date=datetime.today())
               contact.save()
               messages.success(request, "Your Message Has been sent.")
          except:
               messages.error(request, "Your Message Has been sent.")
     return render(request,'contact.html')
# def contacts(request):
#      return HttpResponse("this is contacts page")
     