from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import Plant  
from plants.forms import PlantForm
from django.contrib import messages


def home(request:HttpRequest):
    plants = Plant.objects.all()[:5]
    print("hiii", plants)
    return render(request, 'core/home.html', {'plants': plants})
    
   



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

       
        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, 'core/contact.html')




