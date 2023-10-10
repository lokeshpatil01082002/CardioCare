from django.db import models
class MedicalReport(models.Model):
    patient_id = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=10)
    comments = models.TextField()
    report_file = models.ImageField(upload_to='reports/')
    assigned_doctor = models.CharField(max_length=100)  # You can adjust the max_length as needed

    def __str__(self):
        return self.patient_name  # Display patient name as the object's string representation
