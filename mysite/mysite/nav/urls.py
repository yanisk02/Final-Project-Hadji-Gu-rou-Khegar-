from django.urls import path
from .views import MainPageView
from . import views

app_name = 'nav'

urlpatterns = [
    path('', MainPageView.as_view()),
]