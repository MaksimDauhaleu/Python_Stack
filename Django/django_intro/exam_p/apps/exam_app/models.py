from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class LoginManager(models.Manager):
    def reg_validator(self, postData):
        print("post data in models: ", postData)
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        user = User.objects.filter(email = postData['email'])
        if len(user)>0:
            errors["email"] = "Email exist"

        if len(postData['email']) < 10:
            errors['email'] = "Must be at least 10"

        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = "The password must be at least 8 characters."
        
        if postData["conf_password"] != postData["password"]:
            errors["conf_password"] = "Passwords does not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if not user:
            errors['email'] = 'User does not exist'
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                pass
            else:
                errors['password'] = "Wrong Password"
            
        return errors


    def create_validator(self, postData):
        errors = {}

        if len(postData["destination"]) < 3:
            errors["destination"] = "The distination must be at least 3 characters."

        if len(postData["plan"]) < 3:
            errors["plan"] = "The plan must be at least 3 characters."
            
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    conf_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

    def __repr__(self):
        return f"{self.first_name}{self.last_name}{self.email}{self.password}{self.conf_password}"

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    plan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User ,related_name="trips")
    objects = LoginManager()

    def __repr__(self):
        return f"{self.destination}{self.startdate}{self.enddate}{self.plan}"


class Others(models.Model):
    destination = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    plan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User ,related_name="otherss")
    objects = LoginManager()


    def __repr__(self):
        return f"{self.destination}{self.startdate}{self.enddate}{self.plan}"