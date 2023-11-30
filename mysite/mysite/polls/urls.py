from django.urls import path

from . import views

urlpatterns = [
    path("About Us",views.index2, name="index"),
    path("Progress", views.index1, name="index"),
    path("gress", views.index3, name="index")
]