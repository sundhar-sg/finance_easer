from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from django import template
from django.template import loader
from django.http import HttpResponse
from django.db import connections,transaction
from RedCarpetUp_LMS import forms
from RedCarpetUp_LMS import models
from RedCarpetUp_Loan_Managament_System import settings
from django.contrib import messages

def homepage(request) :
    template1 = loader.get_template('Home_Page.html')
    return HttpResponse(template1.render())

def adminservices(request) :
    username = request.session['username']
    return render(request, "Admin_Services.html",{'username': username})

def adminlm(request) :
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * from redcarpetuplmsdb")
    transaction.commit()
    details = cursor.fetchall()
    list_details = list(details)
    final_list = []
    for x in list_details:
        final_list.append(list(x))
    loanid = []
    custfirstname = []
    custlastname = []
    dob = []
    age = []
    agentserviced = []
    loanamount = []
    loantenure = []
    loanroi = []
    monthlyinterest = []
    for i in range(0, len(final_list)):
        loanid.append(final_list[i][0])
        custfirstname.append(final_list[i][1])
        custlastname.append(final_list[i][2])
        dob.append(final_list[i][3])
        age.append(final_list[i][4])
        agentserviced.append(final_list[i][5])
        loanamount.append(final_list[i][6])
        loantenure.append(final_list[i][7])
        loanroi.append(final_list[i][8])
        monthlyinterest.append(final_list[i][9])
    length_list = []
    for y in range(0, len(final_list)):
        length_list.append(y)
    context = {'username': request.session['username'], 'length_list': length_list, 'loan_id': loanid,
               'custfirstname': custfirstname, 'custlastname': custlastname, 'dob': dob, 'age': age,
               'agentserviced': agentserviced, 'loanamount': loanamount, 'loantenure': loantenure, 'loanroi': loanroi,
               'monthlyinterest': monthlyinterest}
    return render(request, "Admin_LM.html", context)

def adminloanapproval(request) :
    cursor = connections['default'].cursor()
    cursor.execute('SELECT COUNT(*) FROM redcarpetuploanrequestsdb')
    count = cursor.fetchone()
    if int(count[0]) >0 :
        cursor.execute('SELECT * FROM redcarpetuploanrequestsdb')
        loan_requests = cursor.fetchall()
        loan_requests_list = list(loan_requests)
        final_loan_requests = []
        for x in loan_requests_list :
            final_loan_requests.append(list(x))
        requestid = []
        custfirstname = []
        custlastname = []
        custdob = []
        custage = []
        agentrequested = []
        requestedamount = []
        requestedtenure = []
        alottedroi = []
        monthlyinterest = []
        for x in final_loan_requests :
            requestid.append(x[0])
            custfirstname.append(x[1])
            custlastname.append(x[2])
            custdob.append(x[3])
            custage.append(x[4])
            agentrequested.append(x[5])
            requestedamount.append(x[6])
            requestedtenure.append(x[7])
            alottedroi.append(x[8])
            monthlyinterest.append(x[9])
        length_list = []
        for i in range(0, len(final_loan_requests)) :
            length_list.append(i)
        context = {'username': request.session['username'], 'length_list': length_list, 'requestid': requestid, 'firstname': custfirstname, 'lastname': custlastname, 'dob': custdob, 'age': custage, 'agentrequested': agentrequested, 'requestedamount': requestedamount, 'requestedtenure': requestedtenure, 'alottedroi': alottedroi, 'monthlyinterest': monthlyinterest, 'count': int(count[0])}
        return render(request, "Admin_Loan_Approval.html", context)
    context = {'username': request.session['username'], 'count': int(count[0])}
    return render(request, "Admin_Loan_Approval.html", context)


def btnapprove(request):
    cursor = connections['default'].cursor()
    cursor.execute('INSERT INTO redcarpetuplmsdb(custloanid, custfirstname, custlastname, dob, age, agentserviced, loanamount, loantenure, loanroi, monthlyinterest) SELECT loanrequestid, loancustfirstname, loancustlastname, custdob, custage, requestedagent, requestedloanamount, requestedloantenure, alottedloanroi, calculatedloaninterest  FROM redcarpetuploanrequestsdb')
    cursor.execute('TRUNCATE TABLE redcarpetuploanrequestsdb')
    transaction.commit()
    return redirect('adminloanapproval')

def btnreject(request) :
    cursor = connections['default'].cursor()
    cursor.execute('TRUNCATE TABLE redcarpetuploanrequestsdb')
    transaction.commit()
    return redirect('adminloanapproval')

def agentservices(request) :
    username = request.session['username']
    return render(request, "Agent_Services.html", {'username': username})

def agentlm(request) :
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * from redcarpetuplmsdb where agentserviced = '{}'".format(request.session['username']))
    transaction.commit()
    details = cursor.fetchall()
    list_details = list(details)
    final_list = []
    for x in list_details:
        final_list.append(list(x))
    loanid = []
    custfirstname = []
    custlastname = []
    dob = []
    age = []
    agentserviced = []
    loanamount = []
    loantenure = []
    loanroi = []
    monthlyinterest = []
    for i in range(0, len(final_list)):
        loanid.append(final_list[i][0])
        custfirstname.append(final_list[i][1])
        custlastname.append(final_list[i][2])
        dob.append(final_list[i][3])
        age.append(final_list[i][4])
        agentserviced.append(final_list[i][5])
        loanamount.append(final_list[i][6])
        loantenure.append(final_list[i][7])
        loanroi.append(final_list[i][8])
        monthlyinterest.append(final_list[i][9])
    length_list = []
    for y in range(0, len(final_list)):
        length_list.append(y)
    context = {'username': request.session['username'], 'length_list': length_list, 'loan_id': loanid,
               'custfirstname': custfirstname, 'custlastname': custlastname, 'dob': dob, 'age': age,
               'agentserviced': agentserviced, 'loanamount': loanamount, 'loantenure': loantenure, 'loanroi': loanroi,
               'monthlyinterest': monthlyinterest}
    return render(request, "Agent_LM.html", context)

def agentloanrequest(request) :
    form = forms.redcarpetuploanrequests(request.POST or None)
    if form.is_valid() :
        form.save()
        request.session['customername'] = request.POST['loancustfirstname'] + " "+ request.POST['loancustlastname']
        return redirect('agentlrsuccessview')

    context = {'form': form, 'username': request.session['username']}
    return render(request, 'Agent_Loan_Request.html', context)

def agentlrsuccess(request) :
    customername = request.session['customername']
    username = request.session['username']
    return render(request, 'Agent_LR_Success.html', {'customername': customername, 'username': username})

def logout(request) :
    del request.session['username']
    return redirect('homeview')

def customerlm(request) :
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * from redcarpetuplmsdb where custfirstname = '{}'".format(request.session['username']))
    transaction.commit()
    details = cursor.fetchall()
    list_details = list(details)
    final_list = []
    for x in list_details :
        final_list.append(list(x))
    loanid = []
    custfirstname = []
    custlastname = []
    dob = []
    age = []
    agentserviced = []
    loanamount = []
    loantenure = []
    loanroi = []
    monthlyinterest = []
    for i in range(0, len(final_list)) :
        loanid.append(final_list[i][0])
        custfirstname.append(final_list[i][1])
        custlastname.append(final_list[i][2])
        dob.append(final_list[i][3])
        age.append(final_list[i][4])
        agentserviced.append(final_list[i][5])
        loanamount.append(final_list[i][6])
        loantenure.append(final_list[i][7])
        loanroi.append(final_list[i][8])
        monthlyinterest.append(final_list[i][9])
    length_list = []
    for y in range(0, len(final_list)) :
        length_list.append(y)
    context = {'username': request.session['username'],'length_list': length_list, 'loan_id': loanid, 'custfirstname': custfirstname, 'custlastname': custlastname, 'dob': dob, 'age': age, 'agentserviced': agentserviced, 'loanamount': loanamount, 'loantenure': loantenure, 'loanroi': loanroi, 'monthlyinterest': monthlyinterest}
    return render(request, "Customer_LM.html", context)

def signupsuccess(request) :
    template9 = loader.get_template('Signup_Success.html')
    return HttpResponse(template9.render())

def signuppage(request) :
    form = forms.signupform(request.POST or None)
    if form.is_valid() :
        userrole = request.POST['usersrole']
        if userrole == 'Customer':
            form.save()
            return redirect('signupsuccessview')
        messages.error(request, "User Role Type is restricted for only Customer")
        return render(request, 'Signup_Page.html')

    context = {'form' : form}
    return render(request,'Signup_Page.html', context)

def loginauth(request) :
    if request.method == 'POST' :
        email = request.POST['emailid']
        passwrd = request.POST['passwrd']
        usersrole = request.POST['usersrole']
        cursor = connections['default'].cursor()
        cursor.execute("SELECT firstname, usersrole from usersdb WHERE email = '{}'".format(email))
        transaction.commit()
        temp = cursor.fetchone()
        request.session['username'] = temp[0]
        request.session['usersrole'] = temp[1]
        try:
            item = models.usersdb.objects.get(firstname=temp[0])
        except ObjectDoesNotExist:
            return HttpResponse('username error')
        if check_password(passwrd, item.passwrd):
            if (usersrole == 'Administrator' and usersrole == request.session['usersrole']) :
                return redirect('adminservices')
            if(usersrole == 'Agent' and usersrole == request.session['usersrole']) :
                return redirect('agentservices')
            if(usersrole == 'Customer' and usersrole == request.session['usersrole']) :
                return redirect('customerlm')
        return render(request, 'Login_Page.html')
    else :
        return render(request, 'Login_Page.html')

