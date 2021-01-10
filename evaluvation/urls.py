"""evaluvation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from evaluvationapp import views
urlpatterns = [
    path('',views.login,name="login"),
    path('admin/', admin.site.urls),
    path('home',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('login1',views.login1,name="login1"),
    path('AddSubject',views.AddSubject,name="AddSubject"),
    path('allocation',views.allocation,name="allocation"),
    path('Faculity',views.Faculity,name="Faculity"),
    path('Addcollege',views.Addcollege,name="Addcollege"),
    path('Packet',views.Packet,name="Packet"),
     path('Packet1',views.Packet1,name="Packet1"),
      path('Packet2',views.Packet2,name="Packet2"),
    path('viewcollege',views.viewcollege,name="viewcollege"),
    path('viewsubject',views.viewsubject,name="viewsubject"),
    path('viewfaculty',views.viewfaculty,name="viewfaculty"),
    path('viewalocation',views.viewalocation,name="viewalocation"),
    path('viewalocation1',views.viewalocation1,name="viewalocation1"),
    path('viewalocation2',views.viewalocation2,name="viewalocation2"),
    path('viewpacket',views.viewpacket,name="viewpacket"),
     path('editcollege',views.editcollege,name="editcollege"),
     path('EditSubject',views.EditSubject,name="EditSubject"),
      path('editaloca',views.editaloca,name="editaloca"),
     path('editfac',views.editfac,name="editfac"),
     path('editpkt',views.editpkt,name="editpkt"),

     path('removefac',views.removefac,name="removefac"),
     path('removepkt',views.removepkt,name="removepkt"),
      path('removealoca',views.removealoca,name="removealoca"),
     path('removecollege',views.removecollege,name="removecollege"),
     path('removesub',views.removesub,name="removesub"),
       path('printslip',views.printslip,name="printslip"),
        path('serious',views.serious,name="serious"),
       path('valuvation',views.valuvation,name="valuvation"),
         path('Firstvalidation',views.Firstvalidation,name="Firstvalidation"),
        path('SecondEvaluvation',views.SecondEvaluvation,name="SecondEvaluvation"),
       path('ThirdEvaluVation',views.ThirdEvaluVation,name="ThirdEvaluVation"),
       path('retrive3',views.retrive3,name="retrive3"),
       path('retrive1',views.retrive1,name="retrive1"),
       path('retrive2',views.retrive2,name="retrive2"),
]
