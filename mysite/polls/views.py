from typing import Any
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import PatientTime, Doctor,PollUser
from django.contrib.auth.models import User
from .forms import ChooseTimeForm
from django.http import HttpResponseRedirect



def doctor_free_times(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
   
    free_times = doctor.free_time.all()
    form = ChooseTimeForm()
    all_patient_times = PatientTime.objects.all() 

        
    return render(request, 'polls/doctor_free_times.html', {'free_hours': free_times, 'form': form, 'all_patient_times': all_patient_times, 'doctor': doctor,})
        


def index(request):
    latest_doctor_list=Doctor.objects.all()
    context={"latest_doctor_list":latest_doctor_list}

    return render(request, "polls/index.html", context)
    


def login(request):
    if request.method == 'GET':
        return render(request, "polls/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user:  
            request.session['username']=user.username
          
            return HttpResponseRedirect("/polls/")
            
        else:
            return render(request, "polls/login.html", context={"error": "wrong login or password"})
        



def register(request):
    if request.method == 'GET':
        return render(request, "polls/register.html")

    else:
   
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()

        PollUser(user=user.save())

        return HttpResponseRedirect("/polls/login")
    

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/polls/login")
