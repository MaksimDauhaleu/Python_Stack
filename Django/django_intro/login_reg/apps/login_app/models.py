from django.db import models

class Regist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    conf_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.first_name}{self.last_name}{self.email}{self.password}{self.conf_password}"

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['email']) < 10:
            if not EMAIL_REGEX.match(postData['email']):         
                errors['email'] = ("Invalid email address!")
        return errors