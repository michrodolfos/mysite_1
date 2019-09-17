from django.contrib import admin
from .models import Radiologist, Calendar, SuggestedCalendar, Patient, RadiologyCommand, FinalSchedule


# Register your models here.


admin.site.register(Calendar)
admin.site.register(SuggestedCalendar)
admin.site.register(Radiologist)

admin.site.register(Patient)
admin.site.register(RadiologyCommand)
admin.site.register(FinalSchedule)