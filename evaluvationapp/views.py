from django.shortcuts import render
from django.http import HttpResponseRedirect
import pymysql
con=pymysql.connect("localhost","root","","questionpaper")
cur=con.cursor()
# Create your views here.
def home(request):
    return render(request,"index.html")
def login1(request):
    return render(request,"login1.html")
def login(request):
    if(request.POST):
        uname=request.POST.get("t1")
        password=request.POST.get("t2")
    
        qry="select count(*) from login where username='"+uname+"' and password='"+password+"'"
        cur.execute(qry)
        data=cur.fetchall()
        if(data[0][0]==0):
            msg="Invalid username or password"
        else:
            msg="Success"
            return HttpResponseRedirect("/Addcollege")

        con.commit()

    return render(request,"Login.html")
def AddSubject(request):
    
    if(request.POST):
        name=request.POST.get("t1")
        sem=request.POST.get("t2")
        qry="insert into subject_info (subject_name,semester) values('"+str(name)+"','"+str(sem)+"')"
        cur.execute(qry)
        con.commit()
    return render(request,"AddSubject.html")
def allocation(request):
    qry2="select * from subject_info"
    cur.execute(qry2)
    data=cur.fetchall()
    qry3="select * from faculty_info"
    cur.execute(qry3)
    data1=cur.fetchall()
   
    if(request.POST):
        packetid=request.POST.get("t1")
      
        subject=request.POST.get("t3")
        faculty=request.POST.get("t4")
        noofpaper=request.POST.get("t5")
        qry="insert into alocation_info (packet_id,subject_id,faculty_id,noofpapers) values('"+str(packetid)+"','"+str(subject)+"','"+str(faculty)+"','"+str(noofpaper)+"')"
        cur.execute(qry)
        con.commit()
    return render(request,"alocation.html",{"data":data,"data1":data1})
def Faculity(request):
    qry2="select * from subject_info"
    cur.execute(qry2)
    data=cur.fetchall()
    qry3="select * from `college_info`"
    cur.execute(qry3)
    data3=cur.fetchall()
    
    if(request.POST):
        name=request.POST.get("t1")
        college=request.POST.get("t2")
        mailid=request.POST.get("t3")
        phone=request.POST.get("t4")
        subject=request.POST.get("t5")
        sem=request.POST.get("t6")
        qry="insert into faculty_info (name,college,Mail_id,Phone_No,Subject_Id,Semester) values('"+str(name)+"','"+str(college)+"','"+str(mailid)+"','"+str(phone)+"','"+str(subject)+"','"+str(sem)+"')"
        cur.execute(qry)
        con.commit()
    return render(request,"Faculity.html",{"data":data,"data3":data3})
def Addcollege(request):
    if(request.POST):
        name=request.POST.get("t1")
        
        qry="insert into college_info (college_name) values('"+str(name)+"')"
        cur.execute(qry)
        con.commit()
    return render(request,"Addcollege.html")
def Packet(request):
    sem=request.GET.get("sem")
    qry2="select * from subject_info where semester='"+str(sem)+"'"
    cur.execute(qry2)
    data=cur.fetchall()
    qry4="select * from serious where sem='"+str(sem)+"'"
    cur.execute(qry4)
    data4=cur.fetchall()
    msg=""
    if(request.POST):
        seri=request.POST.get("seri")
        packetid=request.POST.get("t1")
        
        subject=request.POST.get("t3")
        noofpaper=request.POST.get("t4")
        
        qry3="select faculty_id  from faculty_info where Subject_Id='"+subject+"' and faculty_id not in(select faculty_id from alocation_info1 ) and faculty_id not in(select faculty_id from alocation_info2 )"
        cur.execute(qry3)
        data1=cur.fetchall()
        if (data1):
            print(data1)
            
        
            faculty=data1[0][0]
            qry="insert into alocation_info (packet_id,subject_id,faculty_id) values('"+str(packetid)+"','"+str(subject)+"','"+str(faculty)+"')"
            cur.execute(qry)
            qry="insert into packet_info (packet_id,semester,subject_id,noofpaper) values('"+str(packetid)+"','"+str(sem)+"','"+str(subject)+"','"+str(noofpaper)+"')"
            cur.execute(qry)
        else:
            msg="No Faculty available"    
        
        con.commit()
    return render(request,"Packet.html",{"data":data,"msg":msg,"data4":data4})
def Packet2(request):
    sem=request.GET.get("sem")
    qry2="select * from subject_info where semester='"+str(sem)+"'"
    cur.execute(qry2)
    data=cur.fetchall()
    qry4="select * from serious where sem='"+str(sem)+"'"
    cur.execute(qry4)
    data4=cur.fetchall()
    msg=""
    if(request.POST):
        seri=request.POST.get("seri")
        packetid=request.POST.get("t1")
        
        subject=request.POST.get("t3")
        noofpaper=request.POST.get("t4")
        qqry="select "
        qry3="select faculty_id  from faculty_info where Subject_Id='"+subject+"' andand faculty_id not in(select faculty_id from alocation_info ) and faculty_id not in(select faculty_id from alocation_info2 )"
        cur.execute(qry3)
        data1=cur.fetchall()
        if (data1):
            print(data1)
            #qqry="select s.subject_name from subject_info join alocation"
        
            faculty=data1[0][0]
            qry="insert into alocation_info2 (packet_id,subject_id,faculty_id) values('"+str(packetid)+"','"+str(subject)+"','"+str(faculty)+"')"
            cur.execute(qry)
            qry="insert into packet_info (packet_id,semester,subject_id,noofpaper) values('"+str(packetid)+"','"+str(sem)+"','"+str(subject)+"','"+str(noofpaper)+"')"
            cur.execute(qry)
        else:
            msg="No Faculty available"    
        
        con.commit()
    return render(request,"Packet2.html",{"data":data,"msg":msg,"data4":data4})
def Packet1(request):
    sem=request.GET.get("sem")
    qry2="select * from subject_info where semester='"+str(sem)+"'"
    cur.execute(qry2)
    data=cur.fetchall()
    qry4="select * from serious where sem='"+str(sem)+"'"
    cur.execute(qry4)
    data4=cur.fetchall()
    msg=""
    if(request.POST):
        seri=request.POST.get("seri")
        packetid=request.POST.get("t1")
        
        subject=request.POST.get("t3")
        noofpaper=request.POST.get("t4")
        
        qry3="select faculty_id  from faculty_info where Subject_Id='"+subject+"' and faculty_id not in(select faculty_id from alocation_info1 ) and faculty_id not in(select faculty_id from alocation_info )"
        cur.execute(qry3)
        data1=cur.fetchall()
        if (data1):
            print(data1)
            
        
            faculty=data1[0][0]
            qry="insert into alocation_info1 (packet_id,subject_id,faculty_id) values('"+str(packetid)+"','"+str(subject)+"','"+str(faculty)+"')"
            cur.execute(qry)
            qry="insert into packet_info (packet_id,semester,subject_id,noofpaper) values('"+str(packetid)+"','"+str(sem)+"','"+str(subject)+"','"+str(noofpaper)+"')"
            cur.execute(qry)
        else:
            msg="No Faculty available"    
        
        con.commit()
    return render(request,"Packet1.html",{"data":data,"msg":msg,"data4":data4})
def viewcollege(request):
    qry="select * from college_info"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewcollege.html",{"data":data})
def viewsubject(request):
    qry="select * from subject_info"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewsubject.html",{"data":data})
def viewfaculty(request):
    qry="select * from faculty_info join subject_info on (faculty_info.Subject_id=subject_info.subject_id)"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewfaculty.html",{"data":data})
def viewalocation(request):
    qry="select a.alocation_id,a.packet_id,s.subject_name,f.name from   alocation_info a join  subject_info s on(a.subject_id=s.subject_id) join  faculty_info f on(f.faculty_id=a.faculty_id)"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewalocation.html",{"data":data})
def viewalocation1(request):
    qry="select a.alocation_id,a.packet_id,s.subject_name,f.name from   alocation_info1 a join  subject_info s on(a.subject_id=s.subject_id) join  faculty_info f on(f.faculty_id=a.faculty_id)"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewalocation1.html",{"data":data})
def viewalocation2(request):
    qry="select a.alocation_id,a.packet_id,s.subject_name,f.name from   alocation_info2 a join  subject_info s on(a.subject_id=s.subject_id) join  faculty_info f on(f.faculty_id=a.faculty_id)"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewalocation.html",{"data":data})
def viewpacket(request):
    qry="select * from packet_info"
    cur.execute(qry)
    data=cur.fetchall()
    return render(request,"viewpacket.html",{"data":data})
def editcollege(request):
    id=request.GET.get("id")
    qry="select * from college_info where college_id='"+str(id)+"'"
    cur.execute(qry)
    data=cur.fetchall()
    if(request.POST):
        id=request.POST.get("t1")
        name=request.POST.get("t2")
        qry2="update college_info set college_name='"+str(name)+"' where college_id='"+str(id)+"'"
        cur.execute(qry2)
        con.commit()
    return render(request,"editcollege.html",{"data":data})
def EditSubject(request):
    id=request.GET.get("id")
    qry="select * from subjecte_info where subject_id='"+str(id)+"'"
    cur.execute(qry)
    data=cur.fetchall()
    if(request.POST):
        id=request.POST.get("t3")
        name=request.POST.get("t1")
        sem=request.POST.get("t2")
        qry2="update subject_info set Subject_name='"+str(name)+"', semester='"+str(sem)+"' where subjecte_id='"+str(id)+"'"
        cur.execute(qry2)
        con.commit()
    return render(request,"EditSubject.html",{"data":data})
def editaloca(request):
    qry="select * from faculty_info "
    cur.execute(qry)
    data2=cur.fetchall()
    qry2="select * from subject_info"
    cur.execute(qry2)
    data1=cur.fetchall()
    id=request.GET.get("id")
    qry="select a.*,s.subject_name from alocation_info a join subject_info s on(s.subject_id=a.subject_id) where alocation_id='"+str(id)+"'"
    cur.execute(qry)
    data=cur.fetchall()
    if(request.POST):
        id=request.POST.get("t6")
        packet=request.POST.get("t1")
       
        faculty=request.POST.get("t4")
        no=request.POST.get("t5")
        qry2="update alocation_info set packet_id='"+str(packet)+"', faculty='"+str(faculty)+"',noofpapers='"+str(no)+"' where alocation_id='"+str(id)+"'"
        cur.execute(qry2)
        con.commit()
    return render(request,"editalocation.html",{"data":data,"data1":data1,"data2":data2})
def editfac(request):
    id=request.GET.get("id")
    qry="select * from faculty_info where faculty_id='"+str(id)+"'"
    cur.execute(qry)
    data=cur.fetchall()
    qry1="select * from Subject_info "
    cur.execute(qry1)
    data1=cur.fetchall()
    if(request.POST):
        id=request.POST.get("t7")
        name=request.POST.get("t1")
        college=request.POST.get("t2")
        mail=request.POST.get("t3")
        pno=request.POST.get("t4")
        sub=request.POST.get("t5")
        sem=request.POST.get("t6")
        qry2="update faculty_info set name='"+str(name)+"',college='"+str(college)+"', Mail_id='"+str(mail)+"',Phone_No='"+str(pno)+"',Subject_Id='"+str(sub)+"',Semester='"+str(sem)+"' where faculty_id='"+str(id)+"'"
        cur.execute(qry2)
        con.commit()
    return render(request,"editFaculity.html",{"data":data,"data1":data1})
def editpkt(request):
    id=request.GET.get("id")
    qry="select * from packet_info where packet_id='"+str(id)+"'"
    cur.execute(qry)
    data=cur.fetchall()
    if(request.POST):
        id=request.POST.get("t1")
        count=request.POST.get("t2")
        subject_id=request.POST.get("t3")
        no=request.POST.get("t4")
       
        qry2="update packet_info set count='"+str(count)+"',subject_id='"+str(subject_id)+"', noofpaper='"+str(no)+"' where packet_id='"+str(id)+"'"
        cur.execute(qry2)
        con.commit()
    return render(request,"editPacket.html",{"data":data})
def removefac(request):
    id=request.GET.get("id")
    qry="delete  from Faculty_info where faculty_id='"+str(id)+"'"
    cur.execute(qry)
    con.commit()
    return HttpResponseRedirect("viewfaculty")
def removepkt(request):
    id=request.GET.get("id")
    qry="delete  from packet_info where packet_id='"+str(id)+"'"
    cur.execute(qry)
    con.commit()
    return HttpResponseRedirect("viewpacket")
def removealoca(request):
    id=request.GET.get("id")
    qry="delete  from alocation_info where alocation_id='"+str(id)+"'"
    cur.execute(qry)
    con.commit()
    return HttpResponseRedirect("viewalocation")
def removecollege(request):
    id=request.GET.get("id")
    qry="delete  from college_info where college_id='"+str(id)+"'"
    cur.execute(qry)
    con.commit()
    return HttpResponseRedirect("viewcollege")
def removesub(request):
    id=request.GET.get("id")
    qry="delete  from subjecte_info where subject_id='"+str(id)+"'"
    cur.execute(qry)
    con.commit()
    return HttpResponseRedirect("viewsubject")
def printslip(request):
    qry="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info.* from alocation_info join subject_info on(alocation_info.subject_id=subject_info.subject_id) join faculty_info on(alocation_info.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info.packet_id)"
    cur.execute(qry)
    data=cur.fetchall()
    
    qry1="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info1.* from alocation_info1 join subject_info on(alocation_info1.subject_id=subject_info.subject_id) join faculty_info on(alocation_info1.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info1.packet_id)"
    cur.execute(qry1)
    data1=cur.fetchall()
    
    qry2="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info2.* from alocation_info2 join subject_info on(alocation_info2.subject_id=subject_info.subject_id) join faculty_info on(alocation_info2.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info2.packet_id)"
    cur.execute(qry2)
    data2=cur.fetchall()
    return render(request,"printslip.html",{"data":data,"data2":data2,"data1":data1})
def Firstvalidation(request):
    qry="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info.* from alocation_info join subject_info on(alocation_info.subject_id=subject_info.subject_id) join faculty_info on(alocation_info.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info.packet_id)"
    cur.execute(qry)
    data=cur.fetchall()
    
    
    return render(request,"Firstvalidation.html",{"data":data})
def SecondEvaluvation(request):
    qry1="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info1.* from alocation_info1 join subject_info on(alocation_info1.subject_id=subject_info.subject_id) join faculty_info on(alocation_info1.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info1.packet_id)"
    cur.execute(qry1)
    data1=cur.fetchall()
    
    
    return render(request,"SecondEvaluvation.html",{"data1":data1})
def ThirdEvaluVation(request):
    qry2="select subject_info.subject_name,faculty_info.name,packet_info.noofpaper,alocation_info2.* from alocation_info2 join subject_info on(alocation_info2.subject_id=subject_info.subject_id) join faculty_info on(alocation_info2.faculty_id=faculty_info.faculty_id) join packet_info on(packet_info.packet_id=alocation_info2.packet_id)"
    cur.execute(qry2)
    data2=cur.fetchall()
    
    
    return render(request,"ThirdEvaluVation.html",{"data2":data2})
def serious(request):
    if request.POST :
        sem=request.POST.get("sem")
        ser=request.POST.get("t1")
        qry="insert into serious (sem,serious) values('"+str(sem)+"','"+str(ser)+"')"
        cur.execute(qry)
        con.commit()
    return render(request,"addserios.html")
def valuvation(request):
    if request.POST :
        typ=request.POST.get("type")
        print("haiiiiiiiiiiiiiiiiiiiiii")
        print(typ)
        if typ=="First":
            sem=request.POST.get("sem")
            return HttpResponseRedirect("Packet?sem="+str(sem))
        if typ=="Second":
            sem=request.POST.get("sem")
            return HttpResponseRedirect("Packet1?sem="+str(sem))
        if typ=="Third":
            sem=request.POST.get("sem")
            return HttpResponseRedirect("Packet2?sem="+str(sem))
    return render(request,"Valuvation.html")
