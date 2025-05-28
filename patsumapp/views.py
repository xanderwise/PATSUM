from django.shortcuts import render, redirect

from patsumapp.models import Tel


# Create your views here.

def starter(request):
    return render(request, 'starter-page.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        mycontact = Tel(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')
