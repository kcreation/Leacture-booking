#tkinter app
from Tkinter import *
import time
import calendar
import random
win=Tk()
win.geometry("1000x1000")
m=Label(win,bd=30,bg="dark slate grey",fg="WHITE",font="Times",text="VN LECTURE")
m.pack()
sumt=0

def cm1():
  u=e1.get()
  nom=e2.get()
  cm=Tk()
  cm.geometry("1000x1000")
  if u.isalpha() and nom.isdigit() and len(nom)==10:
    if str(so)==e3.get():
      def counte():
         global sumt
         sumt=sumt+120
              
      q1=["","red","grey","yellow","dark slate grey","blue","orange","green","cyan","deep pink","midnight blue"]
      for i in range(1,11):
          for j in range(25,0,-1):
              w=Checkbutton(cm,bg=q1[i],fg="black",bd="20",command=counte)
              w.grid(row=i,column=j)
      k=Button(cm,bd=10,bg="green",text="BOOK YOUR SEAT",command=p)
      k.grid(row=15,column=11)
      scr=Label(cm,bg="black",fg="white",font="Times",bd=10,text="------STAGE THIS WAY -------")
      scr.grid(row=18,column=11)
      cm.mainloop()
    else:
      otperr=Label(cm,bg="red",fg="black",font="Times",bd=60,text="------@ *OTP MISMATCH ERROR*@-------""\n""PLS. TRY AGAIN BY ENTERING THE CAREFULLY WITHOUT SPACE""\n""IF PROBLEM PERSIST CONTACT US AT : 8807-924-084 OR EMAIL US AT movizoo@gmail.com")
      otperr.pack()
  else:
      err=Label(cm,bg="red",fg="black",font="Times",bd=60,text="------@ INVALID USERNAME OR PASSWORD @-------""\n""PLS. TRY AGAIN BY ENTERING A USERNAME CONTAINING ALPHABETS AND MOBILE NUMBER CONTAINING 10 DIGITS ""\n""IF PROBLEM PERSIST CONTACT US AT : 8807-924-084 OR EMAIL US AT movizoo@gmail.com")
      err.pack()
      
      
def os():
   finlas=Tk()
   doneby=Label(finlas,bd=50,bg="black",fg="white",font="Times",text="PRESENTED BY :) TEAM VN@NARAYANAN ")
   doneby.pack()
   finlas.mainloop()

def final():
   fin=Tk()
   fin.geometry("1000x1000")
   lala1=Label(fin,bd=40,bg="yellow",font="Times",text=" HAS  SUCCESSFULLY BOOKED YOUR LECTURE TICKETS!!! AT")
   lala1.pack()
   lala2=Label(fin,bd=40,bg="yellow",font="Times",text=time.ctime())
   lala2.pack()
   lala3=Label(fin,bd=40,bg="yellow",font="Times",text="FOR"+e1.get()+"+"+str((sumt-120)//120))
   lala3.pack()
   lala4=Label(fin,bd=40,bg="yellow",font="Times",text="YOUR TICKET NUMBER IS : "+str(random.randint(1000,9999)))
   lala4.pack()
   last=Label(fin,bd=40,bg="midnight blue",fg="white",font="Times",text=" A MESSAGE HAS BEEN SENT TO YOUR REGISTERED MOBILE NUMBER "+str(e2.get()))
   last.pack()
   feed=Label(fin,bd=30,bg="pink",font="Times",text="PLS. GIVE US YOUR FEEDBACK @ VN@gmail.com")
   feed.pack()
   button=Button(fin,bd=30,bg="black",fg="white",text="EXIT",command=os)
   button.pack()
   fin.mainloop()
  
    
def cm3():
   cmcash=Tk()
   cmcash.geometry("1000x1000")
   info=Label(cmcash,bd=30,bg="green",font="Times",text=" YOU HAVE BEEN DIRECTED TO  SECURE+e-cash window.PLS. SELECT YOUR  BANK FOR PAYMENT PROCESS")
   info.pack()
   v=IntVar()
   v1=IntVar()
   v2=IntVar()
   v3=IntVar()
   v4=IntVar()
   v5=IntVar()
   v6=IntVar()
   b1=Radiobutton(cmcash,fg="blue",bd=20,font="Times",text="SBI BANK",variable=v,value=1)
   b1.pack()
   b2=Radiobutton(cmcash,fg="DeepPink3",bd=20,font="Times",text="ICICI BANK",variable=v1,value=2)
   b2.pack()
   b3=Radiobutton(cmcash,fg="blue",bd=20,font="Times",text="BANK OF BARODA",variable=v2,value=3)
   b3.pack()
   b4=Radiobutton(cmcash,bd=20,fg="DeepPink3",font="Times",text="MODERN BANK",variable=v3,value=4)
   b4.pack()
   b5=Radiobutton(cmcash,fg="blue",bd=20,font="Times",text="CENTRAL BANK OF INDIA",variable=v4,value=5)
   b5.pack()
   b6=Radiobutton(cmcash,bd=20,fg="DeepPink3",font="Times",text="AXIS BANK",variable=v5,value=6)
   b6.pack()
   b7=Radiobutton(cmcash,fg="blue",bd=20,font="Times",text="SWISS BANK",variable=v6,value=7)
   b7.pack()
   pay=Button(cmcash,bd=30,bg="green",font="Times",text="$$$           /- PAY -/            $$$",command=final)
   pay.pack()
   process=Label(cmcash,bd=20,bg="red",fg="white",font="Times",text="TRANSACTION UNDER PROCESS~~~Pls. DON'T refresh the page")
   process.pack()
   cmcash.mainloop()
def noto():
   nototo=Tk()
   nototo.geometry("500x500")
   feed=Label(nototo,bd=30,bg="pink",font="Times",text="PLS. GIVE US YOUR FEEDBACK @ VN@gmail.com")
   feed.pack()
   doneby=Label(nototo,bd=30,bg="pink",font="Times",text="PRESENTED BY :) TEAM VN @ krish")
   doneby.pack()
   nototo.mainloop()
   
   
def p():
      cm2 =Tk()
      cm2.geometry("1000x1000")
      lab1=Label(cm2,bg="black",fg="white",bd=30,font="Bold ",text="VN HAS SUCCESSFULLY RESERVED YOUR SEATS FOR RUPEES:-")
      lab1.pack()
      lab2=Label(cm2,bg="yellow",bd=50,font="Times",text=str(sumt)+"-/-only")
      lab2.pack()
      cash=Button(cm2,bd=20,bg="green",font="Times",text="PROCEED FOR PAYMENT",command=cm3)
      cash.pack()
      no=Button(cm2,bd=20,bg="red",fg="yellow",font="Times",text="BACK",command=noto)
      no.pack()
      cm2.mainloop()
def od():
  f=Tk()
  u=e1.get()
  nom=e2.get()
  f.geometry("100x100")
  if u.isalpha() and nom.isdigit() and len(nom)==10:
      kop=Label(f,bg="gold",bd=100,text="NEW MESSAGE RECIEVED""\n"" FROM,TEAM VN""\n"" YOUR OTP IS : " + str(so))
      kop.pack()
      f.mainloop()
  else:
     err1=Label(f,bg="red",fg="black",font="Times",bd=60,text="------@ INVALID USERNAME OR PASSWORD @-------""\n""PLS. TRY AGAIN BY ENTERING A USERNAME CONTAINING ALPHABETS AND MOBILE NUMBER CONTAINING 10 DIGITS ""\n""IF PROBLEM PERSIST CONTACT US AT : 8807-924-084 OR EMAIL US AT movizoo@gmail.com")
     err1.pack()
     f.mainloop()  
  
el1=Label(win,text="USERNAME:")
el1.pack()
e1=Entry(win,bd=5)
e1.pack()
el2=Label(win,text="MOBILE NUMBER (FOR OTP VERIFICATION) :")
el2.pack()
e2=Entry(win,bd=5)
e2.pack()
sm=Button(win,bd=10,bg="orange",font="Times",text="SEND OTP",command=od)
sm.pack()
el3=Label(win,text="OTP IS SEND TO YOUR MOBILE NUMBER :")
el3.pack()
so=random.randint(1000,9999)
e3=Entry(win,bd=5)
e3.pack()
cal=Label(win,bd=10,bg="black",fg="white",font="Times",text=calendar.month(2017,3))
cal.pack()
f1=Button(win,bd=10,bg="yellow",font="Times",text="THE LABOUR LAW",command=cm1)
f2=Button(win,bd=10,bg="cyan",font="Times",text="THE FAMILY LAW",command=cm1)
f1.pack()
f2.pack()
f3=Button(win,bd=10,bg="yellow",font="Times",text="CRIMINAL LAW",command=cm1)
f4=Button(win,bd=10,bg="cyan",font="Times",text="ENVIRONMENTAL LAW",command=cm1)
f3.pack()
f4.pack()
f5=Button(win,bd=10,bg="yellow",font="Times",text="LAW OF TORTS",command=cm1)
f6=Button(win,bd=10,bg="cyan",font="Times",text="LAW OF CONTRACT",command=cm1)
f5.pack()
f6.pack()
win.mainloop()
