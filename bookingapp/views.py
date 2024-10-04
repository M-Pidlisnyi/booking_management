from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from datetime import datetime

from .models import Flight, PlaneSeat, Passenger

# Create your views here.
def index(request):
    
    flights = Flight.objects.all()


    return render(request, "bookingapp/index.html", {"flight_list": flights})


@login_required
def reserve_seat(request: HttpRequest):
    if request.method == "POST":
        flight_id =request.POST.get("flight")
        passenger_username= request.POST.get("passenger")
        booking_time = request.POST.get("booking_time")
    
        PlaneSeat.objects.create(
            flight = Flight.objects.get(id=flight_id),
            passenger = Passenger.objects.get(user__username=passenger_username),
            booking_time=booking_time
        )

        return redirect("reserve")

    return render(request, "bookingapp/reserve_seat.html")

def seats(request: HttpRequest):
    seats = PlaneSeat.objects.filter(booking_time__gt=datetime.now())

    return render(request, "bookingapp/reserved_seats.html", {"seats":seats})