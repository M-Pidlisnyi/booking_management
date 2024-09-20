from django.urls import path
from .views import index, reserve_seat

#booking/
urlpatterns = [
    path("", index, name="index"),
    path("reserve/", reserve_seat, name="reserve"),
]