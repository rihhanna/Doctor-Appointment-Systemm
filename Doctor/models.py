from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class doctors(models.Model):
    shift_options = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'), 
    ]
    Doctor_fields= [
        ('OB/GYN', 'OB/GYN'),
        ('Pediatrician', 'Pediatrician'),
        ('Dermatologist', 'Dermatologist'),
        ('Cardiologist', 'Cardiologist'),
        ('Orthopedist', 'Orthopedist'), 
    ]
    
    POSITION_OPTIONS = [
        ('Senior Consultant', 'Senior Consultant'),
        ('Registrar', 'Registrar'),
        ('Resident', 'Resident'),
        ('Intern', 'Intern'), 
    ]

    fullname = models.CharField(max_length=100)
    shift = models.CharField(max_length=50, choices=shift_options)
    speciality = models.CharField(max_length=100, choices=Doctor_fields)
    position = models.CharField(max_length=50, choices=POSITION_OPTIONS)

    def __str__(self):
        return self.fullname

class Appointment(models.Model):

    doctor = models.ForeignKey(doctors, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.fullname} on {self.appointment_date} at {self.appointment_time}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed for your patient profile

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_patient(sender, instance, **kwargs):
    try:
        instance.patient.save()
    except Patient.DoesNotExist:
        Patient.objects.create(user=instance)



class Image(models.Model):
    Scan_type= [
        ('MRI Scan', 'MRI Scan'),
        ('CT Scan', 'CT Scan'),
        ('MRA Scan', 'MRA Scan'),
        ('PET Scan', 'PET Scan'),
        ('X-ray Scan', 'X-ray Scan'), ]
    title = models.CharField(max_length=100 ,choices=Scan_type)
    Patient_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')


    def str(self):
        return self.title
    

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='contacts/images/')

    def str(self):
        return f"{self.first_name} {self.last_name}"