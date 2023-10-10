from django import forms
from .models import MedicalReport  

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport  # Specify the model here
        fields = ['patient_id', 'patient_name', 'patient_age', 'patient_gender', 'comments', 'report_file', 'assigned_doctor']
