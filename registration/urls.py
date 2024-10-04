from django.urls import path, include

from .views import register_view

#register/
urlpatterns = [
    path("", register_view, name="register"),
    path("", include("django.contrib.auth.urls")),
]