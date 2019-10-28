from django.contrib import admin
from .models import Sneaker, CartSneakers, Checkout
# Register your models here.
admin.site.register(Sneaker)
admin.site.register(CartSneakers)
admin.site.register(Checkout)