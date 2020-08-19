from django.shortcuts import render,redirect

def index(request):
   return render(request,"first_page/index.html")

def services(request):
   return render(request,"first_page/services.html")

def pricing(request):
   return render(request,"first_page/pricing.html")

