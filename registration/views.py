from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from ..bookingapp.models import Passenger

# Create your views here.
def register_view(request: HttpRequest):
   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            new_user = form.save()
            # new_passenger = Passenger.objects.create(user=new_user)
            return redirect("index")
    else: 
        form = UserCreationForm()


    return render(request, "registration/register.html", {"form":form})