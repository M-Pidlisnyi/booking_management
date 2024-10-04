from django.urls import path
from .views import index, reserve_seat, seats

#booking/
urlpatterns = [
    path("", index, name="index"),
    path("reserve/", reserve_seat, name="reserve"),
    path("seats/", seats, name="seats"),
    #path("new-path2/", new_view2, name="tryvcb"),
    #path("new-path3/", new_view2, name="uwernb"),
]
