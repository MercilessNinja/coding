from tkinter import *
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()

l1=[]

def count():
    global c
    c=ent.get()
    cur.execute("update candidates set canvote=canvote+1 where canno={}".format(c))
    con.commit()
def finish():
    buttond.config(state=DISABLED)
    global root3
    root3=Tk()
    labul=Label(root3,text="do you want to confirm")
    labul.grid(row=0,column=0)
    buten=Button(root3,text="yes",fg="white",bg="green",command=lambda:[count(), root3.destroy()])
    buten.grid(row=0,column=1)
    buten2=Button(root3,text="no",fg="white",bg="red",command=root3.destroy)
    buten2.grid(row=0,column=2)
    root3.mainloop()
root2=Tk()
labbel=Label(root2,text="select candidate to vote")
labbel.pack()
cur.execute("select * from candidates")
res=cur.fetchall()
for v in res:
    laabel=Label(root2,text=str(v[0])+'-'+v[1]+"\t("+v[3]+")")
    laabel.pack()
ent=Entry(root2)
ent.pack()
ent.insert(0,"enter candidate number")
buttond=Button(root2,text="next",command=lambda:[finish()])
buttond.pack()
root2.mainloop()
