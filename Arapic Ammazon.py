from tkinter import *
from tkinter import ttk
from datetime import*
from openpyxl import*
from openpyxl import workbook
from PIL import Image,ImageTk
p=1
m={0:['a',20],
   1:['b',10],
   2:["c",30],
   3:['d',15],
  
   
   
   
   
   }
gem=Tk()

pop=gem.iconbitmap()
tr=Frame(gem,height=1100,width=800,bg='gray')
tr.place(y=1,x=1230)
yr=ttk.Treeview(tr,selectmode="browse")
yr.place(x=1,y=1,width=400,height=20)
yr["columns"]=("1","2","3")
yr.column('#0',width=5,anchor='c')
yr.column('#1',width=8,anchor='c')
yr.column('#2',width=12,anchor='c')
yr.column('#3',width=16,anchor='c')
yr.heading('#0',text='tools',anchor='c')
yr.heading('#1',text='coast',anchor='c')
yr.heading('#2',text='total',anchor='c')
yr.heading('#3',text='',anchor='c')
              
        
def fatora():
      gem.geometry('1000x1000')
      Ff=Frame(gem,bg='black',width=5,height= 1)
      Ff.place(x=1,y=1)
      total=0
      for i in yr.get_children():
                yr.delete(i)
                for it in range (len (rt)):
                        if (int(rt[it].get())>0):
                                plo=int(rt[it].get())*m[it][1] 
                        total=total+plo
                mlk=(str(m[it][1]),str(rt[it].get()),str(plo))
                yr.insert("",'end',iid=it,text=m[it][1],values=mlk)
                finall=total

                
                gem.geometry('1000x1000')
                f=Frame(gem,bg='black',width=200,height=1100)
                lio=Label(text="buyer name",height=20,width=80,bg='white',fg='black')         
                lio.place(x=100,y=1)
                eio=Entry(f,bg='white',fg='black',width=180,justify=CENTER)
                eio.place(x=1200,y=6)
                jio=Label(text="buyer numper",height=20,width=80)         
                jio.place(x=100,y=21)











F= Frame(gem,bg="#328E6E",height=1000,width=1100)
F.place(x=1,y=1)


d=Label(gem,text='web for sell tools', fg="gold" ,bg="black",width=145,height=3)
d.place(x=0,y=0)
iop=PhotoImage(file="download.png",)
iol=PhotoImage(file="images(1).png",height=50*3,width=50*5)
iou=PhotoImage(file="bah.png")
#iok=PhotoImage(file="mages(1).png")
oa=Button(relief=SOLID,cursor="hand2",image=iop,width=200,height=150)
oa.place(y=110,x=20)
ob=Button(relief=SOLID,cursor="hand2",image=iol,width=200,height=150)
ob.place(x=200,y=110)
oc=Button(relief=SOLID,cursor="hand2",image=iou,width=200,height=150,)
oc.place(x=400,y=110)
od=Button(relief=SOLID,cursor="hand2",image=iop)
od.place(x=80,y=110)


print("hjrjh")
rt=[]
font1=('Tajwal 12')
TR=IntVar()
R1=IntVar()
R3=IntVar()
R4=IntVar()


rt1=Spinbox(F  ,from_=0 ,to=20,width=10,textvariable=TR,font=font1)
rt1.place(x=130,y=510)
rt.append(rt1)
rt2=Spinbox(F  ,from_=0 ,to=20,width=10,textvariable=R1,font=font1)
rt2.place(x=250,y=510)
rt.append(rt2)
rt3=Spinbox(F  ,from_=0 ,to=20,width=10,textvariable=R3,font=font1)
rt3.place(x=370,y=510)
rt.append(rt3)
rt4=Spinbox(F  ,from_=0 ,to=20,width=10,textvariable=R4,font=font1)
rt4.place(x=490,y=510)
rt.append(rt4)
#bio=Entry(f,bg='white',fg='black',width=180,justify=CENTER)
#bio.place(x=1500,y=26)
#io=Label(text="buyer",height=20,width=80)         
#io.place(x=1500,y=41)
#zio=Entry(f,bg='white',fg='black',width=180,justify=CENTER)
#zio.place(x=1500,y=46)
#kio=Label(text="buyer location",height=20,width=80)         
#kio.place(x=1500,y=61)
#rio=Entry(f,bg='white',fg='black',width=180,justify=CENTER)
#rio.place(x=1500,y=66)
#gio=Label(text="total",height=20,width=80)         
#gio.place(x=1500,y=81)
#eio=Entry(f,bg='white',fg='black',width=180,justify=CENTER,takefocus=mlk)
#eio.place(x=1500,y=86)
def bol():
        print(86959500)





R=Button(bg="gray",width=10,height=3,relief=SOLID,cursor="hand2",text="buy",fg="white",command=fatora )
R.place(x=10,y=700
        )




gem.mainloop()