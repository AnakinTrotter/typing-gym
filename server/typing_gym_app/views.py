from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import pyrebase, bcrypt
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
    if 'user_id' not in request.session:
            request.session['user_id'] = ""
    if not database.child('Users').child(request.session['user_id']).get().val() == "None":
         return HttpResponse("Not logged in")
    else:
        logedInName = database.child('Users').child(request.session['user_id']).child('Username').get().val()

    return HttpResponse(logedInName)
def logout(request):
    request.session['user_id'] = ""
    return redirect("/login")


def login(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST['username_input'])
        if len(user) <= 0:
            messages.error(request, "The username does")
            return redirect("/login")
        if bcrypt.checkpw(request.POST['password_input'].encode(), user[0].password.encode()):
            request.session['user_id'] = request.POST['username_input']
            return redirect("/")
        else:
            print(user[0].password.encode())
            messages.error(request, "Incorrect username or password.")
            return redirect("/login")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        user = User.objects.filter(username=request.POST['username_input'])
        if len(user) > 0:
            messages.error(request, "Username already taken.")
            return redirect("/register")
        pw_hash = bcrypt.hashpw(
            request.POST["password_input"].encode(), bcrypt.gensalt()).decode()
        name = request.POST["username_input"]
        database.child('Users').child(name).set({
                "Highest Score" : 1,
                "Leaderboard positions" : {
                    "Position 1" : 1
                       },
                "Password" : pw_hash,
                "Username" : request.POST["username_input"],
                "Word List" : {
                    "the": 0,
                    "be": 0,
                    "of": 0,
                    "and": 0,
                    "a": 0,
                    "to": 0,
                    "in": 0,
                    "he": 0,
                    "have": 0,
                    "it": 0,
                    "that": 0,
                    "for": 0,
                    "they": 0,
                    "I": 0,
                    "with": 0,
                    "as": 0,
                    "not": 0,
                    "on": 0,
                    "she": 0,
                    "at": 0,
                    "by": 0,
                    "this": 0,
                    "we": 0,
                    "you": 0,
                    "do": 0,
                    "but": 0,
                    "from": 0,
                    "or": 0,
                    "which": 0,
                    "one": 0,
                    "would": 0,
                    "all": 0,
                    "will": 0,
                    "there": 0,
                    "say": 0,
                    "who": 0,
                    "make": 0,
                    "when": 0,
                    "can": 0,
                    "more": 0,
                    "if": 0,
                    "no": 0,
                    "man": 0,
                    "out": 0,
                    "other": 0,
                    "so": 0,
                    "what": 0,
                    "time": 0,
                    "up": 0,
                    "go": 0,
                    "about": 0,
                    "than": 0,
                    "into": 0,
                    "could": 0,
                    "state": 0,
                    "only": 0,
                    "new": 0,
                    "year": 0,
                    "some": 0,
                    "take": 0,
                    "come": 0,
                    "these": 0,
                    "know": 0,
                    "see": 0,
                    "use": 0,
                    "get": 0,
                    "like": 0,
                    "then": 0,
                    "first": 0,
                    "any": 0,
                    "work": 0,
                    "now": 0,
                    "may": 0,
                    "such": 0,
                    "give": 0,
                    "over": 0,
                    "think": 0,
                    "most": 0,
                    "even": 0,
                    "find": 0,
                    "day": 0,
                    "also": 0,
                    "after": 0,
                    "way": 0,
                    "many": 0,
                    "must": 0,
                    "look": 0,
                    "before": 0,
                    "great": 0,
                    "back": 0,
                    "through": 0,
                    "long": 0,
                    "where": 0,
                    "much": 0,
                    "should": 0,
                    "well": 0,
                    "people": 0,
                    "down": 0,
                    "own": 0,
                    "just": 0,
                    "because": 0,
                    "good": 0,
                    "each": 0,
                    "those": 0,
                    "feel": 0,
                    "seem": 0,
                    "how": 0,
                    "high": 0,
                    "too": 0,
                    "place": 0,
                    "little": 0,
                    "world": 0,
                    "very": 0,
                    "still": 0,
                    "nation": 0,
                    "hand": 0,
                    "old": 0,
                    "life": 0,
                    "tell": 0,
                    "write": 0,
                    "become": 0,
                    "here": 0,
                    "show": 0,
                    "house": 0,
                    "both": 0,
                    "between": 0,
                    "need": 0,
                    "mean": 0,
                    "call": 0,
                    "develop": 0,
                    "under": 0,
                    "last": 0,
                    "right": 0,
                    "move": 0,
                    "thing": 0,
                    "general": 0,
                    "school": 0,
                    "never": 0,
                    "same": 0,
                    "another": 0,
                    "begin": 0,
                    "while": 0,
                    "number": 0,
                    "part": 0,
                    "turn": 0,
                    "real": 0,
                    "leave": 0,
                    "might": 0,
                    "want": 0,
                    "point": 0,
                    "form": 0,
                    "off": 0,
                    "child": 0,
                    "few": 0,
                    "small": 0,
                    "since": 0,
                    "against": 0,
                    "ask": 0,
                    "late": 0,
                    "home": 0,
                    "interest": 0,
                    "large": 0,
                    "person": 0,
                    "end": 0,
                    "open": 0,
                    "public": 0,
                    "follow": 0,
                    "during": 0,
                    "present": 0,
                    "without": 0,
                    "again": 0,
                    "hold": 0,
                    "govern": 0,
                    "around": 0,
                    "possible": 0,
                    "head": 0,
                    "consider": 0,
                    "word": 0,
                    "program": 0,
                    "problem": 0,
                    "however": 0,
                    "lead": 0,
                    "system": 0,
                    "set": 0,
                    "order": 0,
                    "eye": 0,
                    "plan": 0,
                    "run": 0,
                    "keep": 0,
                    "face": 0,
                    "fact": 0,
                    "group": 0,
                    "play": 0,
                    "stand": 0,
                    "increase": 0,
                    "early": 0,
                    "course": 0,
                    "change": 0,
                    "help": 0,
                    "line": 0
                }
        })
        user = User.objects.create(
            username=request.POST["username_input"], password=pw_hash)
    return render(request, 'register.html')