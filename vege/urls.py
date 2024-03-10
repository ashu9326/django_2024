from django.urls import path
from . import views

urlpatterns = [
    path('receipe/',views.receipe, name='vege/receipe'),
]