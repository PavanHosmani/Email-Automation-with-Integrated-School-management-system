import email
import mysql.connector as sql
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
import smtplib
from requests import request
def register(request):
    email=""
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lasttname')
        rollnumber=request.POST.get('Roll_number')
        email=request.POST.get('email')
        std=request.POST.get('class')
        max_fees=request.POST.get('max_fees')
        paid_fees=request.POST.get('paid_fees')
        m=sql.connect(host="localhost",user="root",passwd="******#",database="school")
        cursor=m.cursor()
        c="insert into school values('{}','{}','{}','{}','{}','{}','{}')".format(firstname,lastname,rollnumber,std,email,max_fees,paid_fees)
        cursor.execute(c)
        m.commit()
        return render(request,'register.html',{'fn':firstname})
    return render(request,'register.html')

def showrecords(request):
    con=sql.connect(host='localhost',user='root',password='Pawanking9945#',database='school')
    cur=con.cursor()
    cur.execute("SELECT * FROM school")
    records=cur.fetchall()
    datafromdb=[]
    for i in records:
        datafromdb.append(list(i))
    return render(request,'record.html',{'yo':datafromdb})

def send_mail(request):
    con=sql.connect(host='localhost',user='root',password='Pawanking9945#',database='school')
    cur=con.cursor()
    cur.execute("SELECT * FROM school")
    records=cur.fetchall()
    l=[]
    for i in records:
        if i[5]>i[6]:
            l.append([i[0],i[1],(i[5]-i[6])])
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("wodgemusic1@gmail.com", "nstwpknecylnknej")
            message = "Hi,This Message is to inform that your child "+ i[0] +" Fees is Pending ,kindly Request is pay the Fees "+str((i[5]-i[6]))
            s.sendmail("wodgemusic1@gmail.com",i[4], message)
            s.quit()
    return render(request,'email.html',{'l':l})


def console(request):
    return render(request,'console.html')
