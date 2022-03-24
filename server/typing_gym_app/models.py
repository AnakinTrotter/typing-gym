from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
# use the django default user for the user
# ideas: burst generates one, type asap, Typing test: 2 min timer, type until the wpm goes down past a certain level, Practice: need 100% accuracy, if you miss you need to retype 3 times
# Look ahead: as they type a word it disappears, if they get a word wrong it reshows up, a counter will go up and count which whords they missed the most, have a leaderboard for players.
class MyAccountManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(
            username=username,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email_Address, password):
        user = self.create_user(
            Email_Address=self.normalize_email(Email_Address),
            password=password,
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Users(AbstractBaseUser):
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_super_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Username'

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.username)


    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser




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