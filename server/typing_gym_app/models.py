from django.db import models

class User(models.Model):
  username = models.CharField(max_length=12)
  password = models.TextField()

# Create your models here.
# use the django default user for the user
# ideas: burst generates one, type asap, Typing test: 2 min timer, type until the wpm goes down past a certain level, Practice: need 100% accuracy, if you miss you need to retype 3 times
# Look ahead: as they type a word it disappears, if they get a word wrong it reshows up, a counter will go up and count which whords they missed the most, have a leaderboard for players. 

#endpoints:
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


# model:
# words will be generated through the front end
# store accuracy results in json, let the sorting get handled by user's computer
# Accuracy results will consist of each word that is possible to generate (around 300), 
#Api should return something like this
#{
  #"govern": {
  #  "count": 100,
   # "correct": 99
  # },
 # "next word"...
#}
# Having user will return all the information needed for each word, authentication information
# Using Rest framework, you can use the Serializer to return the model object
# Need an Account manager, AbstractBaseUser model, Registration Serializer
