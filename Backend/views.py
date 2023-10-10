
from django.shortcuts import render
import pyrebase




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
def UpoloadReportPage(request):
   
    if request.method == 'POST':
        form = MedicalReportForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the data to the Django model
            report = form.save()

            # Push the data to Firebase Realtime Database
            data = {
                'patient_id': report.patient_id,
                'patient_name': report.patient_name,
                'patient_age': report.patient_age,
                'patient_gender': report.patient_gender,
                'comments': report.comments,
                'assigned_doctor': report.assigned_doctor,
                # You can add more fields if needed
            }
            database.child('medical_reports').push(data)  # 'medical_reports' is the Firebase database path

            # You can add a success message or redirect to a thank you page
            return redirect('thank_you_page')  # Redirect to a thank you page
    else:
        form = MedicalReportForm()

    return render(request, 'uploadreport.html', {'form': form})
 