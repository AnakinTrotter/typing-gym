from dis import dis
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib import messages
# Create your models here.
# use the django default user for the user
# ideas: burst generates one, type asap, Typing test: 2 min timer, type until the wpm goes down past a certain level, Practice: need 100% accuracy, if you miss you need to retype 3 times
# Look ahead: as they type a word it disappears, if they get a word wrong it reshows up, a counter will go up and count which whords they missed the most, have a leaderboard for players.
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        try:
            if len(post_data["username_input"]) > 15:
                errors["username_input"] = "Username should be 15 characters long or less."
            elif len(post_data["username_input"]) < 2:
                errors["username_input"] = "Username should be at least 2 characters long."
            if len(post_data["password_input"]) < 8:
                errors["password_input"] = "Password should be at least 8 characters long."
        except:
            errors["unknown_error"] = "An unknown error has occured."
        return errors


class User(models.Model):
    objects = UserManager()
    username = models.CharField(max_length=15)
    name = models.TextField(default="Anonymous Typing Gymnast")
    password = models.TextField()
    #to make add a submission make a new submission with user as its user


class Submission(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wpm = models.IntegerField(default=0)
    accuracy = models.FloatField(default=100)
    dissapearing = models.IntegerField(default=0)

    #not certain if this is how u override for django argh
    def __gt__(self, other):
        return (self.wpm > other.wpm) if (self.wpm != other.wpm) else ((self.accuracy > other.accuracy) if self.accuracy != other.accuracy else (self.dissapearing > other.dissapearing))

    def __eq__(self, other):
        return (self.wpm == other.wpm and self.accuracy == other.accuracy and self.dissapearing == other.dissapearing)



# endpoints:
# GETS:
# /leaderboard/int, only returns data from users with accuracy of number or higher, sorted by wpm > accuracy > amount of words disappearing, when they click a button it'll call this one
# /leaderboard, all users sorted by wpm > accuracy > amount of words disappearing
# /register
# /login
# /logout
# /user/string Returns all user information for the given username in a json file
# POSTS:
# /leaderboard/update, Check if user is logged in with the authentication token, update learderboard position
# /user/update, Called after each round, update word counts, and check if user has a new high record
# /user/update/highscore, Called after each round, update high score


# model:
# words will be generated through the front end
# store accuracy results in json, let the sorting get handled by user's computer
# Accuracy results will consist of each word that is possible to generate (around 300),
# Api should return something like this
# {
# "govern": {
#  "count": 100,
# "correct": 99
# },
# "next word"...
# }
# Having user will return all the information needed for each word, authentication information
# Using Rest framework, you can use the Serializer to return the model object
# Need an Account manager, AbstractBaseUser model, Registration Serializer
# Swapping to using firebase db
# "Users": {
#   "User1": {
#       "Username" : temp, "Password" : temp, "Highest score" : 1,
#       "Leaderboad Positions" {
#           "Position Number" : 1, 
#        }
#       "Word List" : {
#           "word1" : 1, "word 2" : 2, etc.    
#       }
#   }
# }

#"Leaderboard": {
#   "position 1": {
#       "WPM" : 1, "accuracy" : 100%, "words disappeared" : 1, "Username" : username
#   }
# }