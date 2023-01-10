from django.urls import path

#from same directory import views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rose", views.rose, name="rose"),
    path("<str:name>", views.greet, name="greet")
]
