from django import forms
from RedCarpetUp_Loan_Managament_System import models

class signupform(forms.ModelForm) :
    class Meta :
        model = models.usersdb1
        fields = ["firstname", "lastname", "dob", "age", "usersrole", "email", "mobileno", "passwrd", "confirmpass"]

class redcarpetuploanrequests(forms.ModelForm) :
    class Meta :
        model = models.redcarpetuploanrequestsdb1
        fields = ["loanrequestid", "loancustfirstname", "loancustlastname", "custdob", "custage", "requestedagent", "requestedloanamount", "requestedloantenure", "requestedloanroi", "calculatedloaninterest"]