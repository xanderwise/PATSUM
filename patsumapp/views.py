from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from PATSUMBUSSINESS import settings
from patsumapp.models import Tel


# Create your views here.

def starter(request):
    return render(request, 'starter-page.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def contact(request):
    selected_plan = request.GET.get('plan', '')  # Get the selected plan from the URL if present

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save to database
        mycontact = Tel(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        mycontact.save()

        # Send email notification
        full_message = f"""
        New Contact Form Submission:

        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        send_mail(
            subject=f"New Contact Message: {subject}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent. Thank you!")
        return redirect('/contact')

    return render(request, 'contact.html', {
        'selected_plan': selected_plan
    })
