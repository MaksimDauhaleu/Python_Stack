from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class RegistManager(models.Manager):
    def reg_validator(self, postData):
        print("post data in models: ", postData)
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        user = Regist.objects.filter(email = postData['email'])
        if len(user)>0:
            errors["email"] = "Email exist"

        if len(postData['email']) < 10:
            errors['email'] = "Must be at least 10"

        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = "The password must be at least 8 characters."
        
        if postData["conf_password"] != postData["password"]:
            errors["conf_password"] = "Password dont match"
        return errors

    def login_validator(self, postData):
        # print(postData['password'])
        errors = {}
        user = Regist.objects.filter(email = postData['email'])
        print("encode pw from db", user[0].password.encode()) 
        password = postData['password']
        print("encode pw from form",password.encode())
        if not user:
            errors['email'] = 'User does not exist'
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                pass
            else:
                errors['password'] = "Wrong Passwprd"
            
        return errors
        
        




class Regist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    conf_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistManager()

    def __repr__(self):
        return f"{self.first_name}{self.last_name}{self.email}{self.password}{self.conf_password}"


