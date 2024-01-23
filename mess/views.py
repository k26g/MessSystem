from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import food
# Create your views here.
def home(request):
    return render(request,"index.html")
def login(request):
    if request.method =='GET':
        a=request.GET.get('un')
        b=request.GET.get('pwd')
        fd=list(food.objects.filter(username=a).values())
        if len(fd)>0 and fd[0]["password"]==b:
            print(fd,a,b,"Hello")
            return render(request,"index.html")
        else:
            return render(request,"login.html")
        # return HttpResponse(fd)
    return render(request,"login.html")
def order_form(request):
    return render(request,"order-form.html")
def register(request):
     if request.method == 'POST':
                fd=food()
                fd.username= request.POST.get('username')
                fd.email= request.POST.get('email')
                fd.phone= request.POST.get('phone')
                fd.password= request.POST.get('password')
                try :
                    fd.save()       
                    return render(request, 'login.html')
                except:
                    return HttpResponse("Already Exists")
     else:
                return render(request,'register.html')
     