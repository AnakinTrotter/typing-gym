from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config={
    "apiKey": "AIzaSyCRiJQ8cqSSz82Uz8Z6OnbHsyMHt1yySRc",
    "authDomain": "typing-gym.firebaseapp.com",
    "projectId": "typing-gym",
    "storageBucket": "typing-gym.appspot.com",
    "messagingSenderId": "395816540003",
    "appId": "1:395816540003:web:b4abdd2e8041bd55966556",
    "measurementId": "G-MQRWL4SJ80"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def index(request):
    return HttpResponse('Working!')
