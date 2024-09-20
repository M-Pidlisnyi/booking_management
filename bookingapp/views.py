from django.shortcuts import redirect, render
from .models import Flight, PlaneSeat, Passenger

# Create your views here.
def index(request):
    
    flights = Flight.objects.all()


    return render(request, "bookingapp/index.html", {"flight_list": flights})


def reserve_seat(request):
    if request.method == "POST":
        flight_id =request.POST.get("flight")
        passenger_username= request.POST.get("passenger")
    
        PlaneSeat.objects.create(
            flight = Flight.objects.get(id=flight_id),
            passenger = Passenger.objects.get(user__username=passenger_username)
        )

        return redirect("reserve")

    return render(request, "bookingapp/reserve_seat.html")