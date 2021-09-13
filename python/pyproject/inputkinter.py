from tkinter import *
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()

l1=[]
def linsearch(l,x):
    f=0
    for i in range(len(l)):

        if l[i]==x:
            f=1
            return (f)
    else:
        return (f)

def count(n):
    cur.execute("update candidates set canvote=canvote+1 where canno={}".format(n))
    con.commit()
    
def finish():
    buttond.config(state=DISABLED)
    global root3
    global c
    c=ent.get()
    while int(c)<=n and int(c)>0:
        root5=Tk()
        root5.title("confirmation")
        root5.geometry("200x100")
        labul=Label(root5,text="do you want to confirm")
        labul.grid(row=0,column=0)
        buten=Button(root5,text="yes",fg="white",bg="green",command=lambda:[count(c), root5.destroy()])
        buten.grid(row=0,column=1)
        buten2=Button(root5,text="no",fg="white",bg="red",command=root5.destroy)
        buten2.grid(row=0,column=2)
        root5.mainloop()
        break
    else:
        labul=Label(root2,text="invalid candidate number")
        labul.pack()

def idfication():
    global b
    global result
    global root2
    global buttond
    global ent
    b=g.get()
    result=linsearch(l1,int(b))
    if result==1:
        mybutton2.config(state=DISABLED)
        root3=Tk()
        root3.geometry("300x300")
        root3.title("verification result")
        labl2=Label(root3,text="not eligible")
        labl2.pack()
        button3=Button(root3,text="exit",command=root3.destroy,bg="black",fg="white")
        button3.pack()
        root3.mainloop()
    if result==0:
        mybutton2.config(state=DISABLED)
        root2=Tk()
        root2.title("casting vote")
        root2.geometry("600x900")
        labbel=Label(root2,text="candidate list:-")
        labbel.pack()
        cur.execute("select * from candidates")
        res=cur.fetchall()
        for v in res:
            laabel=Label(root2,text=str(v[0])+'-'+v[1]+"\t("+v[3]+")")
            laabel.pack()
        ent=Entry(root2, width=30)
        ent.pack()
        ent.insert(0,"enter candidate number")
        buttond=Button(root2,text="next",command=lambda:[finish()],bg="black",fg="white")
        buttond.pack()
        root2.mainloop()
        l1.extend([int(b)])
        

def age():
    global a
    global g
    global mybutton2
    a=e.get()
    if int(a)>=18:
        mybutton.config(state=DISABLED)
        root1=Tk()
        root1.geometry("300x300")
        root1.title("id verification")
        g=Entry(root1, width=30)
        g.pack()
        g.insert(0,"enter voter id")
        mybutton2=Button(root1,text="next",command=lambda:[idfication()],bg="black",fg="white")
        mybutton2.pack()
        root1.mainloop()
    else:
        root4=Tk()
        labl1=Label(root4,text="you cannot vote,please try again")
        labl1.pack()
        buttons=Button(root4,text="exit",command=root4.destroy,bg="black",fg="white")
        buttons.pack()
        
n=2 
h=0
l=0
b=""
a=""
while True:
    root=Tk()
    root.geometry("300x300")
    root.title("age verification")
    labbeel=Label(root,text="enter your age")
    labbeel.pack()
    e=Entry(root, width=30)
    e.pack()
    mybutton=Button(root,text="next",command=lambda:[age()],bg="black",fg="white")
    mybutton.pack()
    root.mainloop()







