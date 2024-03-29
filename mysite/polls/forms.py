from django import forms
from .models import PatientTime, Appointment

class ChooseTimeForm(forms.ModelForm):
    class Meta:
        model = PatientTime
        fields = ['time']

class ChooseAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['time']