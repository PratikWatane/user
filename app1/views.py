from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        sallary = request.POST.get("sallary")
        designation = request.POST.get("designation")
        is_active = request.POST.get("is_active")
        if is_active == "yes":
            is_active = True
        else:
            is_active = False
        User.objects.create(name = name,age= age, sallary= sallary, designation=designation, is_active=is_active)
           
        return redirect("home_page")
    elif request.method == 'GET':
        return render(request,"home.html")
    
def show_deails(request):
    obj = User.objects.all()
    return render(request, "show.html", context={"user_data":obj})