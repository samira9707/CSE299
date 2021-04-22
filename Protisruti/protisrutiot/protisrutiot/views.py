from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.http import HttpResponse
import pyrebase

config = {
    'apiKey': "AIzaSyDuEOTHTtVqf3qVHHBjEZJM2u2uStNgAL0",
    'authDomain': "protisruti0.firebaseapp.com",
    'databaseURL': "https://protisruti0-default-rtdb.firebaseio.com",
    'projectId': "protisruti0",
    'storageBucket': "protisruti0.appspot.com",
    'messagingSenderId': "965893934891",
    'appId': "1:965893934891:web:a04fdee508d76df0633f6e",
    'measurementId': "G-BP8GN37Y3R"
  }
firebase = pyrebase.initialize_app(config)
authe = firebase.auth() 
database=firebase.database()

def fetchdata(request):
    most= database.child("LastUpdate").child("Moisture").get().val()
    light= database.child("LastUpdate").child("Light").get().val()
    time = database.child("LastUpdate").child("Time").get().val()
    temp = database.child("LastUpdate").child("temp").get().val()
    """
    d= database.child("Data").shallow().get().val()
    date=[]
    
    for i in d:
        date.append(i)
    ldr=[]
    moisture=[]
    
    temp=[]
    time=[]
    for i in date:
        
        moist= database.child("LastUpdate").child(i).child("Moisture").get().val()
        light= database.child("Data").child(i).child("ldr").get().val()
        tmp= database.child("Data").child(i).child("temp").get().val()
        tm= database.child("Data").child(i).child("Time").get().val()

        ldr.append(light)
        moisture.append(moist)
        temp.append(tmp)
        time.append(tm)
        rudesamira = zip(ldr,moisture,temp,time)
    """
    return render(request,'home.html',{'most':most,'light':light,'Time':time,'temp':temp})

def otp(request):

    return render(request,'otp.html')
    
def login(request):
    return render(request,'login.html')