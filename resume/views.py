from django.contrib.auth import authenticate,login,logout
from resume.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from ownblog.settings import EMAIL_HOST_USER
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ownblog.settings import account_sid,auth_token,my_twilio
from twilio.rest import Client

def Home(request):
    if request.method == "POST":
        d = request.POST
        name = d['name']
        zemail = d['email']
        zsubject = d['subject']
        zmessage = d['message']
        email = 'tejendrapatel1998@gmail.com'
        subject = "You Tejendra You Have a Contact Enquirey "
        content = "Contact Enquirey"
        try:
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            d = {'name': name, 'zemail': zemail ,'zsubject':zsubject ,'zmessage':zmessage}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('home')
        except:
            return render(request,'index.html')