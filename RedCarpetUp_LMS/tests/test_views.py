from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse

class TestViews(TestCase) :
    def setUp(self):
        self.client = Client()

    def test_homeview(self):
        response = self.client.get(reverse('homeview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home_Page.html')

    def test_signupview(self):
        response = self.client.get(reverse('signupview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Signup_Page.html')

    def test_signupsuccessview(self):
        response = self.client.get(reverse('signupsuccessview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Signup_Success.html')

    def test_adminservicesview(self):
        response = self.client.get(reverse('adminservices'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Admin_Services.html')

    def test_adminlaview(self):
        response = self.client.get(reverse('adminloanapproval'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Admin_Loan_Approval.html')

    def test_adminlmview(self):
        response = self.client.get(reverse('adminlm'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Admin_LM.html')

    def test_agentservicesview(self):
        response = self.client.get(reverse('agentservices'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Agent_Services.html')

    def test_agentlrview(self):
        response = self.client.get(reverse('agentloanrequestview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Agent_Loan_Request.html')

    def test_agentlrsuccessview(self):
        response = self.client.get(reverse('agentlrsuccessview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Agent_LR_Success.html')

    def test_agentlmview(self):
        response = self.client.get(reverse('agentlm'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Agent_LM.html')


class TestViews1(TransactionTestCase):
    def test_loginview(self):
        response = self.client.get(reverse('loginview'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Login_Page.html')

    def test_customerlmview(self):
        response = self.client.get(reverse('customerlm'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Customer_LM.html')