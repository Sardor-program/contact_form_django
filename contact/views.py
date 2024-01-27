from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact



def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)


def success_page(request):
    return render(request, 'success.html')





def messages(request):
    information = Contact.objects.all()
    context = {
        "info": information
    }
    return render(request, 'messages.html', context)

