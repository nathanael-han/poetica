from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.shortcuts import render
from django.urls import reverse


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from poetica.models import User

# Create your views here.
def user_view(request):
    return render(request, 'poetica/index.html')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first"]
        last_name = request.POST["last"]
        picture = request.POST["profile_picture"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/registration.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name, picture=picture)
            user.save()
        except IntegrityError:
            return render(request, "users/registration.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/registration.html")