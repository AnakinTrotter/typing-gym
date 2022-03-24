from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
config = {
  "apiKey": "AIzaSyCRiJQ8cqSSz82Uz8Z6OnbHsyMHt1yySRc",
  "authDomain": "typing-gym.firebaseapp.com",
  "databaseURL": "https://typing-gym-default-rtdb.firebaseio.com",
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
    leader1 = database.child('Leaderboard').child('Position 1').child('Accuracy').get().val()
    return HttpResponse(leader1)
