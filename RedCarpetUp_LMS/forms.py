from django import forms
from RedCarpetUp_LMS import models

class signupform(forms.ModelForm) :
    class Meta :
        model = models.usersdb
        fields = ["firstname", "lastname", "dob", "age", "gender", "usersrole", "email", "mobileno", "passwrd", "confirmpass"]

class redcarpetuploanrequests(forms.ModelForm) :
    class Meta :
        model = models.redcarpetuploanrequestsdb
        fields = ["loanrequestid", "loancustfirstname", "loancustlastname", "custdob", "custage", "requestedagent", "requestedloanamount", "requestedloantenure", "alottedloanroi", "calculatedloaninterest"]