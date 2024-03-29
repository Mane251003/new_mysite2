from django.db import models

from django.contrib.auth.models import User


class PollUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    reqistered_at=models.DateTimeField(auto_now_add=True)
    is_removed=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
   
    is_removed=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class PatientTime(models.Model):
    time=models.DateTimeField(unique=True)
    
    def __str__(self):
        return str(self.time)



class Doctor(models.Model):
    last_name=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    free_time=models.ManyToManyField(PatientTime)


    def __str__(self):

        return f"{self.last_name}- {self.first_name}- {self.profession}"
    


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor} - {self.patient} - {self.time}"


