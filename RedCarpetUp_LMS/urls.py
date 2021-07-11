"""RedCarpetUp_Loan_Managament_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from RedCarpetUp_LMS import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homeview'),
    path('login/', views.loginauth, name='loginview'),
    path('signup/', views.signuppage, name='signupview'),
    path('signup-success/', views.signupsuccess, name='signupsuccessview'),
    path('adminservices/', views.adminservices, name='adminservices'),
    path('adminlm/', views.adminlm, name='adminlm'),
    path('adminloanapproval/', views.adminloanapproval, name='adminloanapproval'),
    path('agentservices/', views.agentservices, name='agentservices'),
    path('agentlm/', views.agentlm, name='agentlm'),
    path('agentloanrequest/', views.agentloanrequest, name='agentloanrequestview'),
    path('agentlrsuccess/', views.agentlrsuccess, name='agentlrsuccessview'),
    path('customerlm/', views.customerlm, name='customerlm'),
    path('logout/', views.logout, name='logoutview'),
    path('adminloanapprove/', views.btnapprove, name='approveview'),
    path('adminloanreject/', views.btnreject, name='rejectview')
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)