from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members),
    path("home/", views.home,name="home"),
    path("test/", views.test),
    path("main/", views.main)
]
