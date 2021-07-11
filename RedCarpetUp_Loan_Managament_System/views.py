from django.shortcuts import render,redirect
from django import template
from django.template import loader
from django.http import HttpResponse
from django.db import connections,transaction
from RedCarpetUp_Loan_Managament_System import forms
from RedCarpetUp_Loan_Managament_System import models
from RedCarpetUp_Loan_Managament_System import settings
from django.contrib import messages
import pickle

def homepage(request) :
    template1 = loader.get_template('Home_Page.html')
    return HttpResponse(template1.render())

def adminservices(request) :
    template2 = loader.get_template('Admin_Services.html')
    return HttpResponse(template2.render())

def adminlm(request) :
    template3 = loader.get_template('Admin_LM.html')
    return HttpResponse(template3.render())

def adminloanapproval(request) :
    template4 = loader.get_template('Admin_Loan_Approval.html')
    return HttpResponse(template4.render())

def agentservices(request) :
    template5 = loader.get_template('Agent_Services.html')
    return HttpResponse(template5.render())

def agentlm(request) :
    template6 = loader.get_template('Agent_LM.html')
    return HttpResponse(template6.render())

def agentloanrequest(request) :
    template7= loader.get_template('Agent_Loan_Request.html')
    return HttpResponse(template7.render())

def customerlm(request) :
    template8 = loader.get_template('Customer_LM.html')
    return HttpResponse(template8.render())

def signuppage(request) :
    form = forms.signupform(request.POST or None)
    if form.is_valid() :
        form.save()
        cursor = connections['default'].cursor()
        cursor.execute("INSERT INTO django_logindb(firstname, lastname, email, passwrd) SELECT DISTINCT firstname, lastname, email, passwrd FROM django_signupdb")
        transaction.commit()

    context = {'form': form}
    return render(request,'Signup_Page.html',context)

def loginauth(request) :
    if request.method == 'POST' :
        if request.POST['emailid'] and request.POST['passwrd'] :
            email = request.POST['emailid']
            passwrd = request.POST['passwrd']
            cursor = connections['default'].cursor()
            usersrole = "SELECT usersrole FROM "
            sql = "SELECT firstname, lastname FROM django_logindb WHERE (email = '{}' AND passwrd = '{}')".format(email, passwrd)
            if (cursor.execute(sql)):
                transaction.commit()
                return redirect('servicesview')
            messages.error(request, "Invalid e-mail or password")
            return render(request, 'Login_Page.html')
        else :
            return render(request, 'Login_Page.html')
    else :
        return render(request, 'Login_Page.html')

