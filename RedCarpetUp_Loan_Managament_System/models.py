from django.db import models

#This database is used to store the details of the different types of users
class usersdb1(models.Model) :
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    age = models.IntegerField(max_length=5)
    usersrole = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mobileno = models.IntegerField(max_length=15)
    passwrd = models.CharField(max_length=20)
    confirmpass = models.CharField(max_length=20)
    class Meta :
        db_table = 'usersdb1'

#This database stores the necessary details of the customers who had loans with our company
class redcarpetuplmsdb1(models.Model) :
    custloanid = models.CharField(max_length=20)
    custfirstname = models.CharField(max_length=20)
    custlastname = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    age = models.IntegerField(max_length=5)
    agentserviced = models.CharField(max_length=20)
    loanamount = models.IntegerField(max_length=10)
    loantenure = models.IntegerField(max_length=5)
    loanroi = models.IntegerField(max_length=5)
    monthlyinterest = models.IntegerField(max_length=10)
    class Meta :
        db_table = 'redcarpetuplmsdb1'

#This database stores the necessary details of the customers who had requested loans with our company through our agents
class redcarpetuploanrequestsdb1(models.Model) :
    loanrequestid = models.CharField(max_length=20)
    loancustfirstname = models.CharField(max_length=20)
    loancustlastname = models.CharField(max_length=20)
    custdob = models.DateField(max_length=20)
    custage = models.IntegerField(max_length=5)
    requestedagent = models.CharField(max_length=20)
    requestedloanamount = models.IntegerField(max_length=10)
    requestedloantenure = models.IntegerField(max_length=5)
    requestedloanroi = models.IntegerField(max_length=5)
    calculatedloaninterest = models.IntegerField(max_length=10)
    class Meta :
        db_table = 'redcarpetuploanrequestsdb1'