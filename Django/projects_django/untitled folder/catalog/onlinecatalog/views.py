from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.contrib.sessions.models import Session
from .forms import *


# Create your views here.
def index(request):
    sneakers = Sneaker.objects.all()
    sneakers = sneakers[:6]
    context = {'sneakers': sneakers}
    return render(request, 'index.html', context)


def detail(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, pk=sneaker_id)
    context = {'sneaker': sneaker}
    return render(request, 'detail.html', context)


def about(request):
    sneakers = Sneaker.objects.all()
    sneaker_about = []
    for sneaker in sneakers:
        if sneaker.id <= 15:
            sneaker_about.append(sneaker)

    context = {'sneakers': sneaker_about}
    return render(request, 'about.html', context)


def catalog(request):
    sneakers = Sneaker.objects.all()
    sneaker_about = []
    for sneaker in sneakers:
        if sneaker.id >= 16:
            sneaker_about.append(sneaker)

    context = {'sneakers': sneaker_about}
    return render(request, 'catalog.html', context)

def login(request):
    return render(request, 'login.html')
    

def regist(request):
   return render(request, 'regist.html')


def user_login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            a = postData['password']
            print(a,"*********")
            return redirect('/login')
        else: 
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/catalog')

def regist_process(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/regist')
        else:
            full_name = request.POST['full_name']
            email = request.POST['email']
            password = request.POST['password']
            dof = request.POST['dof']
            phone = request.POST['phone_number']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(dof = dof, phone_number = phone , full_name = full_name, email = email, password = pw_hash)
            request.session['id'] = user.id
            return redirect('/catalog/')


# def cart(request):
#     return render(request, 'cart.html')

# User.objects.create(full_name= request.POST['full_name'], email= request.POST['email'], dof= request.POST['dof'], phone_number= request.POST['phone_number'], password= request.POST['password'], password_conf= request.POST['password_conf'])


def price_range(request):
    first = request.POST['first']
    second = request.POST['second']
    keds = Sneaker.objects.all()
    rigth_keds = []
    for ked in keds:
        if ked.price >= int(first) and ked.price <= int(second):
            item = ked
            rigth_keds.append(item)


    context = {
        'snks' : rigth_keds,
    }
    return render(request, 'catalog.html', context)

def add_to_cart(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, pk=sneaker_id)
    sessions = Session.objects.all()
    for session in sessions:
        print(session)
    try:
        the_id = request.session["cart_id"]
    except:
        new_cart = CartSneakers()
        new_cart.save()
        request.session["cart_id"] = new_cart.id
        new_cart.sneakers.add(sneaker)
        new_cart.save()
        return redirect('/cart/')

    current_cart = CartSneakers.objects.get(id=the_id)

    if not sneaker in current_cart.sneakers.all():
        current_cart.sneakers.add(sneaker)
        current_cart.save()
        return redirect('/cart/')
    else:
        current_cart.sneakers.remove(sneaker)
        return redirect('/cart/')



def cart(request):
    the_id = request.session["cart_id"]
    current_cart = CartSneakers.objects.get(id=the_id)
    cart_items = current_cart.sneakers.all()
    request.session.set_expiry(100)

    total_price = sum([item.price for item in cart_items])

    context = {'cart_items': cart_items, 'total_price': total_price}

    return render(request, 'cart.html', context)


def checkout(request):
    the_id = request.session["cart_id"]
    current_cart = CartSneakers.objects.get(id=the_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            Checkout.objects.create(cart=current_cart,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            e_mail=form.cleaned_data['e_mail'],
            phone_number=form.cleaned_data['phone_number'],
            address=form.cleaned_data['address'])
        return render(request, 'checkout-done.html', {'order': 'order'})

    else:
        print('GET')
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form})