
from django.shortcuts import render
import pyrebase
from django import forms
from .models import MedicalReport 
from .forms import MedicalReportForm

config={
    "apiKey": "AIzaSyD6rd2GlMmbuMkyeSlke-7j6GwY36SMIO8",
    "authDomain": "sevasadancardiocare.firebaseapp.com",
    "databaseURL": "https://sevasadancardiocare-default-rtdb.firebaseio.com",
    "projectId": "sevasadancardiocare",
    "storageBucket": "sevasadancardiocare.appspot.com",
    "messagingSenderId": "220203105412",
    "appId": "1:220203105412:web:70e07ff83521312b8156d1"
}

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
# email = "scc.wce@gmail.com"
# password = "1234567"
# user=None
# try:
#     user = authe.sign_in_with_email_and_password(email, password)
#     print("Authentication successful!")
#     print("User UID:", user['localId'])  # Access user UID like this
# except Exception as e:
#     print(f"Authentication failed: {str(e)}")

# try:
#     if user:
#         name = database.child('Data').child('Name').get().val()
#         age = database.child('Data').child('Age').get().val()
#         print('hello')
#         print("Name:", name)
#         print("Age:", age)
#     else :
#         print('user is null')
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
# Create your views here.




def LandingPage(request):
    return render(request, 'landingpage.html')

def RegisterPage(request):
    return render(request, 'register.html')
def LogInPage(request):
    return render(request, 'login.html')
def UploadReportPage(request):
    if request.method == 'POST':
        patient_id = request.POST['patientId']
        patient_name = request.POST['patientName']
        patient_age = request.POST['patientAge']
        patient_gender = request.POST['patientGender']
        comments = request.POST['comments']
        assigned_doctor = request.POST['assignDoctor']
        
        # Handle file upload
        report_file = request.FILES['reportFile']
        # You can save the report_file to a cloud storage service or server storage
        
        # Construct data dictionary for Firebase
        data = {
            'patient_id': patient_id,
            'patient_name': patient_name,
            'patient_age': patient_age,
            'patient_gender': patient_gender,
            'comments': comments,
            'assigned_doctor': assigned_doctor,
            # Add other fields as needed
        }
        
        # Push the data to Firebase Realtime Database
        database.child('medical_reports').push(data)  # 'medical_reports' is the Firebase database path
        
        # You can add a success message or redirect to a thank you page
        return render(request, 'uploadreport.html')  # Redirect to a thank you page
    else:
        form = MedicalReportForm()

    return render(request, 'uploadreport.html', {'form': form})
 