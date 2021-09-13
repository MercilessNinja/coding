from tkinter import *
from PIL import ImageTk,Image
import pandas
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
window=Tk()
window.title('voting')
window.geometry('400x500')

l=Label(window,text="voting")
l.pack()
img=ImageTk.PhotoImage(Image.open("voting.png"))
mylabel=Label(image=img)
mylabel.pack()

def buttonfunc():
    cur.execute("select * from candidates")
    result=cur.fetchall()
    headers=["snno","name","vote","symbol"]
    l=[]
    for r in result:
        l.append(r)
    print(pandas.DataFrame(l,None,headers))
    print()

def buttonf():
    print("you can vote now")


b=Button(window,text="click to view candidates",command=buttonfunc)
b.pack()

b1=Button(window,text="click me!!",command=buttonf)
b1.pack()

quiet=Button(window,text='exit',command=window.destroy)
quiet.pack()

window.mainloop()

x=input("enter password")
if x=="hello world":
    print("access granted")
else:
    print("access not granted")
