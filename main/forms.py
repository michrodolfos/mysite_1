from django import forms
from django.forms import ModelForm, formset_factory
from .models import Patient, RadiologyCommand
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name',
                  'last_name',
                  'email',
                  'birthday',
                  'gender',
                  'father_name',
                  'mother_name',
                  'insurance_id',
                  'home_address',
                  'mobile_number',
                  'home_number',
                  'work_number']


class NewDoctorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    doctor_speciality = forms.CharField(label='Doctor Speciality', required=True, max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','doctor_speciality', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(NewDoctorForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NewRadiologyCommandForm(ModelForm):
    class Meta:
        model = RadiologyCommand
        fields = ['patient',
                  'reason',
                  'radiology_amount',
                  'schedule',
                  'priority_level']
