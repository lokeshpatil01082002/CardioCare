
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
email = "scc.wce@gmail.com"
password = "1234567"
user=None
try:
    user = authe.sign_in_with_email_and_password(email, password)
    print("Authentication successful!")
    print("User UID:", user['localId'])  # Access user UID like this
except Exception as e:
    print(f"Authentication failed: {str(e)}")

try:
    if user:
        name = database.child('Data').child('Name').get().val()
        age = database.child('Data').child('Age').get().val()
        print('hello')
        print("Name:", name)
        print("Age:", age)
    else :
        print('user is null')
except Exception as e:
    print(f"An error occurred: {str(e)}")








# Create your views here.
