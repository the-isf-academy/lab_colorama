from django.urls import path
from color_app import views


app_name = "color_app"
urlpatterns = [
    path('', views.home, name="index"),
    path('random/', views.random_color, name="random_color"),
    path('colors/', views.color_list, name="color_list"),
    path('colors/new', views.new_color, name="new_color")
]

