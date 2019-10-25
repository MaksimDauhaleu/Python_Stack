from django import forms
from .models import *


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    e_mail = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
