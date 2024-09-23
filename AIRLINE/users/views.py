from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    # Render halaman utama jika user sudah login
    return render(request, "users/users.html")


def login_view(request):
    if request.method == "POST":
        # Ambil data dari form
        username = request.POST["username"]
        password = request.POST["password"]

        # Autentikasi user
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            # Jika autentikasi sukses, login user dan redirect ke index
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # Jika gagal, kembalikan pesan error
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        # Jika request method adalah GET, render halaman login
       return render(request, "users/login.html")


def logout_view(request):
    # Logout user dan redirect ke halaman login
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
   