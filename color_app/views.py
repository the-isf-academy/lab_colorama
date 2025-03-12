from django.shortcuts import render, redirect
from color_app.models import Color
from random import randint
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy, reverse
from color_app.models import Color
from color_app.forms import ColorForm


def home(request):
    # renders the homepage

    skyblue = Color(name="skyblue", red=135, green=206, blue=250)

    params = {
        "name": "stranger",
        "color": skyblue,
    }
    
    response = render(request, 'color_app/index.html', params)
    return response

def random_color(request):
    # renders a random color

    random_color = Color(
        name="random color", 
        red=randint(0, 256), 
        green=randint(0, 256),
        blue=randint(0, 256)
    )

    params = {"color": random_color}

    return render(request, 'color_app/random_color.html', params)

def color_list(request): 
    # renders all colors in database

    color_list = Color.objects.all()
    params = {"color_list": color_list}

    return render(request, 'color_app/color_list.html', params)

def new_color(request):
    # processes new color form 
    
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("color_app:color_list"))
    else:
        form = ColorForm()
    
    return render(request, "color_app/color_form.html", {"form": form})

