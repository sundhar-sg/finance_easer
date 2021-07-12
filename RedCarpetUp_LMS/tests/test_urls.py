from django.urls import reverse, resolve
from RedCarpetUp_LMS import views
from django.test import SimpleTestCase

class TestURLS(SimpleTestCase) :
    def test_homeview_resolves(self):
        url = reverse('homeview')
        self.assertEquals(resolve(url).func, views.homepage)

    def test_loginview_resolves(self):
        url = reverse('loginview')
        self.assertEquals(resolve(url).func, views.loginauth)

    def test_signupsuccess_resolves(self):
        url = reverse('signupsuccessview')
        self.assertEquals(resolve(url).func, views.signupsuccess)

    def test_signupview_resolves(self):
        url = reverse('signupview')
        self.assertEquals(resolve(url).func, views.signuppage)

    def test_logout_resolves(self):
        url = reverse('logoutview')
        self.assertEquals(resolve(url).func, views.logout)

    def test_adminservices_resolves(self):
        url = reverse('adminservices')
        self.assertEquals(resolve(url).func, views.adminservices)

    def test_adminlr_resolves(self):
        url = reverse('adminloanapproval')
        self.assertEquals(resolve(url).func, views.adminloanapproval)

    def test_adminlm_resolves(self):
        url = reverse('adminlm')
        self.assertEquals(resolve(url).func, views.adminlm)

    def test_agentservices_resolves(self):
        url = reverse('agentservices')
        self.assertEquals(resolve(url).func, views.agentservices)

    def test_agentlm_resolves(self):
        url = reverse('agentlm')
        self.assertEquals(resolve(url).func, views.agentlm)

    def test_agentlr_resolves(self):
        url = reverse('agentloanrequestview')
        self.assertEquals(resolve(url).func, views.agentloanrequest)

    def test_agentlrsuccess_resolves(self):
        url = reverse('agentlrsuccessview')
        self.assertEquals(resolve(url).func, views.agentlrsuccess)

    def test_customerlm_resolves(self):
        url = reverse('customerlm')
        self.assertEquals(resolve(url).func, views.customerlm)

    def test_approve_resolves(self):
        url = reverse('approveview')
        self.assertEquals(resolve(url).func, views.btnapprove)

    def test_reject_resolves(self):
        url = reverse('rejectview')
        self.assertEquals(resolve(url).func, views.btnreject)
