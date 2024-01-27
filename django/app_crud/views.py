from django.shortcuts import render
from .models import User


def home(request):
    return render(request, "html/home.html")


def create_user(request):
    users = {"users": User.objects.all()}
    if request.method == "POST":
        new_user = User()
        print(request.POST)
        new_user.first_name = request.POST.get("first_name")
        new_user.last_name = request.POST.get("last_name")
        new_user.age = int(request.POST.get("age"))
        new_user.save()
        return render(request, "html/users.html", users)
    return render(request, "html/users.html", users)
