from django.shortcuts import render

# Create your views here.

def home(request):

    people = [
        {'name': 'Ashutosh', 'age': 28},
        {'name': 'Sachin', 'age': 40},
        {'name': 'Shubham', 'age': 17},
        {'name': 'Shilpi', 'age': 25},
        {'name': 'Bhoomi', 'age': 12},
        {'name': 'Akul', 'age': 20},
        {'name': 'Shweta', 'age': 8},
    ]
    return render(request,"index.html", context={'page':'Django First Project','people':people})

def contact(request):
    context = {'page':'Contact'}          # page title
    return render(request,"contact.html", context)

def about(request):
    context = {'page':'About Us'}         # page title
    return render(request,"about.html", context)
