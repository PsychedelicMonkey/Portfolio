from django import forms
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'id': 'name'}), max_length=100, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'id': 'email'}), max_length=100, required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'id': 'subject'}), max_length=100, required=100)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'id': 'message', 'rows': 5}), required=True)

def about(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data.get('subject'),
                data.get('body'),
                data.get('email'),
                [settings.ADMIN_EMAIL]
            )
            messages.info(request, 'Thanks for emailing me. Please allow 1-2 days for a response.')
            return redirect('about')
        else:
            messages.error(request, 'There was a problem sending your email. Please try again later.')
            return redirect('about')
    user = User.objects.get(pk=1)
    form = EmailForm()
    context = {
        'title': 'About Me',
        'page': 'about',
        'user': user,
        'form': form,
    }
    return render(request, 'user/about.html', context)

