from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.


class Radiologist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    current_tasks = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Radiologists'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Calendar(models.Model):
    schedule = models.DateTimeField(default=timezone.now, unique=True)

    class Meta:
        verbose_name_plural = "Calendars"

    def __str__(self):
        return f'{self.schedule}'


class SuggestedCalendar(models.Model):
    schedule = models.DateTimeField(default=timezone.now, unique=True)

    class Meta:
        verbose_name_plural = "Suggested Calendars"

    def __str__(self):
        return f'{self.schedule}'


class Patient(models.Model):
    male = 'M'
    female = 'F'
    GENDER_CHOICES = [
        (male, 'Male'),
        (female, 'Female')
    ]

    patient_id = models.AutoField(primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    birthday = models.DateField(default='1970-12-24')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    insurance_id = models.CharField(max_length=50)
    home_address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    home_number = models.CharField(max_length=20, blank=True)
    work_number = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RadiologyCommand(models.Model):
    priority_high = 'H'
    priority_normal = 'N'
    PRIORITY_CHOICES = [
        (priority_normal, 'Normal priority'),
        (priority_high, 'High priority')]

    command_id = models.AutoField(primary_key=True, editable=False, unique=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, default=1, verbose_name='Patients', on_delete=models.SET_DEFAULT)
    reason = models.CharField(max_length=100)
    radiology_amount = models.PositiveIntegerField(default=0)
    schedule = models.ForeignKey(SuggestedCalendar, default=1, verbose_name='Preferred day and time for appointment', on_delete=models.SET_DEFAULT)
    priority_level = models.CharField(max_length=1, default=0, choices=PRIORITY_CHOICES)

    class Meta:
        verbose_name_plural = 'Radiology Commands'

    def __str__(self):
        return f'Radiology Command ID: {self.command_id}, received on {self.date_sent}.'


class FinalSchedule(models.Model):
    date_sent = models.DateTimeField(auto_now_add=True)
    radiologist = models.ForeignKey(Radiologist, default=1, verbose_name='Radiologists', on_delete=models.SET_DEFAULT)
    schedule = models.ForeignKey(Calendar, default=1, verbose_name='Calendars', on_delete=models.SET_DEFAULT)
    radiology_command = models.ForeignKey(RadiologyCommand, default=1, verbose_name='Radiology Commands', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = 'Final Schedules'

    def __str__(self):
        return f'{self.radiology_command} Scheduled on {self.schedule} with {self.radiologist} for {self.radiology_command.patient}.'
