from django.db import models
from django.contrib.auth.hashers import make_password

#This database is used to store the details of the different types of users
class usersdb(models.Model) :
    firstname = models.CharField(max_length=20, primary_key=True)
    lastname = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    usersrole = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mobileno = models.CharField(max_length=15)
    passwrd = models.CharField(max_length=200)
    confirmpass = models.CharField(max_length=200)
    class Meta :
        db_table = 'usersdb'

    def save(self, *args, **kwargs) :
        self.passwrd = make_password(self.passwrd, None, 'pbkdf2_sha256')
        self.confirmpass = make_password(self.confirmpass, None, 'pbkdf2_sha256')
        super(usersdb, self).save(*args, **kwargs)

#This database stores the necessary details of the customers who had loans with our company
class redcarpetuplmsdb(models.Model) :
    custloanid = models.CharField(max_length=20)
    custfirstname = models.CharField(max_length=20)
    custlastname = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    agentserviced = models.CharField(max_length=20)
    loanamount = models.CharField(max_length=10)
    loantenure = models.CharField(max_length=5)
    loanroi = models.CharField(max_length=5)
    monthlyinterest = models.CharField(max_length=10)
    class Meta :
        db_table = 'redcarpetuplmsdb'

#This database stores the necessary details of the customers who had requested loans with our company through our agents
class redcarpetuploanrequestsdb(models.Model) :
    loanrequestid = models.CharField(max_length=20)
    loancustfirstname = models.CharField(max_length=20)
    loancustlastname = models.CharField(max_length=20)
    custdob = models.CharField(max_length=20)
    custage = models.CharField(max_length=5)
    requestedagent = models.CharField(max_length=20)
    requestedloanamount = models.CharField(max_length=10)
    requestedloantenure = models.CharField(max_length=5)
    alottedloanroi = models.CharField(max_length=5)
    calculatedloaninterest = models.CharField(max_length=10)
    class Meta :
        db_table = 'redcarpetuploanrequestsdb'