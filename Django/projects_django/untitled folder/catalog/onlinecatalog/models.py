from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


class LoginManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = User.objects.filter(email = postData['email'])

        if len(postData['full_name']) < 5:
            errors['full_name'] = "First name should be at least 5 characters"

        if len(user)>0:
            errors["email"] = "Email exist"

        if len(postData['email']) < 10:
            errors['email'] = "Must be at least 10"

        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = "The password must be at least 8 characters."
        
        if postData["password_conf"] != postData["password"]:
            errors["password_conf"] = "Passwords does not match"

        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if not user:
            errors['email'] = 'User does not exist'
        else:
            if bcrypt.checkpw(postData['password'].encode('utf-8'), user[0].password.encode()):
                pass
            else:
                errors['password'] = "Wrong Password"
            
        return errors





class Sneaker(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    sneaker_image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=65)
    dof = models.DateField()
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=65)
    password_conf = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

    def __repr__(self):
        return f"{self.full_name}{self.email}{self.dof}{self.phone_number}{self.password}{self.password_conf}"

class CartSneakers(models.Model):
    sneakers = models.ManyToManyField(Sneaker, blank=True)

    def __str__(self):
        return str(self.id)


class Checkout(models.Model):
    cart = models.ForeignKey(CartSneakers, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


    def __str__(self):
        return str(self.id)