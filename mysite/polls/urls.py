
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doctor/<int:doctor_id>/", views.doctor_free_times, name="doctor_free_times"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path("logout/", views.log_out)
]