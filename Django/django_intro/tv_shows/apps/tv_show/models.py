from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=100)
    network =models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title}{self.network}"