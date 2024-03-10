from django.shortcuts import render,redirect
from . models import *
# Create your views here.
# featch data from .html file
def receipe(request):
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_discription = request.POST.get('receipe_discription')
        receipe_image = request.FILES.get('receipe_image')
        # print(receipe_name)
        # print(receipe_discription)
        # print(receipe_image)

        Receipe.objects.create(
        receipe_name = receipe_name,
        receipe_discription = receipe_discription,
        receipe_image =receipe_image
        )

        return redirect('vege/receipe')

# save above data(frontend data) into database
    return render (request, 'receipes.html')