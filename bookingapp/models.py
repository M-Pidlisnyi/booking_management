from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    with_kid = models.BooleanField()
    ...
    
    class Meta:
        db_table = "passengers"
        verbose_name = "Regisetered Flight Passenger"

    def __str__(self) -> str:
        return self.user.username


class Plane(models.Model):
    plane_brand = models.CharField(max_length=50)# Boeing
    plane_model = models.CharField(max_length=50)# 737

    class Meta():
        ordering = ["plane_brand", "plane_model"]

    def __str__(self) -> str:
        return f"{self.plane_brand} {self.plane_model}"



class Flight(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.SET_DEFAULT, default="unknown plane", related_name="flights")
    #maybe add city model
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plane} flights from {self.from_city} to {self.to_city}"

class PlaneSeat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    booking_time = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name = "Seat on the Flight"
        verbose_name_plural = "Seats on the Flight"



