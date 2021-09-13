from tkinter import *
import time
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234")
cur=con.cursor()

l2=[]
l1=[]
def linsearch(l,x):#FUNCTION FOR LINEARSEARCH
    f=0
    for i in range(len(l)):
        if l[i]==x:
            f=1
            return (f)
    else:
        return (f)

def count(n):#function to count vote
    global k
    cur.execute("update {} set canvote=canvote+1 where canno={}".format(topic,n))
    con.commit()
    k=k+1
    l1.extend([int(b)])
    
def finish():#function to verify candidate number 
    global root5
    global c
    c=ent.get()
    buttond.config(state=DISABLED)
    labul=Label(root2,text="please close this window").pack()
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

def idfication():#function for verification of voter id
    global b
    global result
    global root2
    global root3
    global buttond
    global ent
    b=g.get()
    mybutton2.config(state=DISABLED)
    result=linsearch(l1,int(b))
    labuul=Label(root1,text="please close this window").pack()
    if result==1:
        root3=Tk()
        root3.geometry("300x300")
        root3.title("verification result")
        labl2=Label(root3,text="not eligible(already voted)")
        labl2.pack()
        button3=Button(root3,text="exit",command=root3.destroy,bg="black",fg="white")
        button3.pack()
        root3.mainloop()
    if result==0 and int(b)<=vono and int(b)>=1:
        root2=Tk()
        root2.title("casting vote")
        root2.geometry("600x900")
        labbel=Label(root2,text="candidate list:-")
        labbel.pack()
        cur.execute("select * from {}".format(topic))
        res=cur.fetchall()
        for v in res:
            laabel=Label(root2,text=str(v[0])+'-'+v[1]+"\t("+v[3]+")")
            laabel.pack()
        label=Label(root2,text="enter candidate number").pack()
        ent=Entry(root2, width=30)
        ent.pack()
        buttond=Button(root2,text="next",command=lambda:[finish()],bg="black",fg="white")
        buttond.pack()
        root2.mainloop()
    elif int(b)>vono or int(b)<1:
        label1=Label(root1,text="incorrect voter id").pack()
        
def age():#function for verification of age
    global a
    global g
    global mybutton2
    global root1
    mybutton.config(state=DISABLED)
    a=e.get()
    lubul=Label(root,text="please close this window").pack()
    if int(a)>=18:
        root1=Tk()
        root1.geometry("300x300")
        root1.title("id verification")
        label=Label(root1,text="enter voter id").pack()
        g=Entry(root1, width=30)
        g.pack()
        mybutton2=Button(root1,text="next",command=lambda:[idfication()],bg="black",fg="white")
        mybutton2.pack()
        root1.mainloop()
    else:
        lubul=Label(root,text="please close this window").pack()
        root4=Tk()
        labl1=Label(root4,text="you cannot vote(under age)")
        labl1.pack()
        buttons=Button(root4,text="exit",command=lambda:[root4.destroy()],bg="black",fg="white")
        buttons.pack()
#MAIN PROGRAM
topic=input("ENTER VOTING NAME: ")
#CREATION OF DATABASE AND TABLE
cur.execute("create database if not exists vote")
cur.execute("use vote")
cur.execute("drop table if exists {}".format(topic))
cur.execute("create table if not exists {}(canno int,canname char(20),canvote int,cansymbol char(20))".format(topic))
cur.execute("create table if not exists voters(voterid int)")
con.commit()
#INPUT OF CANDIDATE DETAILS
a=0
choice=None
n=int(input("Enter Number Of Candidates: "))
while choice!=0 and a<n:
    print("1.ADD CANDIDATE")
    print("2.SHOW CANDIDATE")
    print("0.EXIT")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        no=int(input("Enter Candidate Number: "))
        result=linsearch(l2,no)#USAGE OF LINEAR SEARCH
        l2.extend([no])
        if result==1:
            print("***INCORRECT CANDIDATE NUMBER(ALREADY ADDED)***")
        if result==0:
            name=input("Enter Candidate Name: ")
            symbol=input("Enter Candidate Symbol: ")
            vote=0
            query1="insert into {} values({},'{}',{},'{}')".format(topic,no,name,vote,symbol)
            cur.execute(query1)
            con.commit()
            print("***CANDIDATE DETAILS ADDED***")
            a+=1
            time.sleep(1)
    elif choice==2:
        query2="select * from {}".format(topic)
        cur.execute(query2)
        result=cur.fetchall()
        print("canNo","%18s"%"Name","%10s"%"Votes")
        for row in result:
            print(row[0],"%20s"%row[1],"%10s"%row[2])
    elif choice==0:
        print("bye!!")
    else:
        print("***INVALID CHOICE***")

time.sleep(3)
#DISPLAYING LIST OF CANDIDATES        
print("Final List Of All Candidates:")
cur.execute("select * from {}".format(topic))
result=cur.fetchall()
print("CanNo","%18s"%"Name","%10s"%"Symbol")
for row in result:
    print(row[0],"%20s"%row[1],"%10s"%row[3])
print("*"*50)
time.sleep(1)
#UPDATION OF CANDIDATE DETAILS
print("##CANDIDATE UPDATION##")
ans='y'
abc=input("DO YOU WANT TO UPDATE??(y/n)")
if abc.lower()=='y':
    while ans.lower()=='y':
        num = int(input("ENTER CANNO TO UPDATE :"))
        query="select * from {} where canno={}".format(topic,num)
        cur.execute(query)
        result = cur.fetchall()
        if cur.rowcount==0:
            print("***Sorry! CanNo not found*** ")
        else:
            print("CANNO","%20s"%"NAME","%10s"%"SYMBOL")
            for row in result:
                print(row[0],"%20s"%row[1],"%10s"%row[3])
            choice=input("\n## ARE YOUR SURE TO UPDATE ? (Y) :")
            if choice.lower()=='y':
                print("## YOU CAN UPDATE ONLY NAME AND SYMBOL ##")
                d = input("ENTER NEW NAME,(LEAVE BLANK IF NOT WANT TO CHANGE): ")
                if d=="":
                    d=row[1]
                try:
                    s = (input("ENTER NEW SYMBOL,(LEAVE BLANK IF NOT WANT TO CHANGE):  "))
                except:
                    s=row[3]
                query="update {} set canname='{}',cansymbol='{}' where canno={}".format(topic,d,s,num)
                cur.execute(query)
                con.commit()
                print("## RECORD UPDATED ## ")
        ans=input("UPDATE MORE (y/n) :")

print("*"*50)
time.sleep(3)
#INPUT OF VOTERS             
vono=int(input("Enter Number Of Voters: "))
for i in range(1,vono+1):
    query5="insert into voters values({})".format(i)
    cur.execute(query5)
    con.commit()
time.sleep(1)
print("*"*50)
 
h=0
l=0
b=""
a=""
k=0
while k<vono:
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

#DECLARATION OF WINNER
query7="select canname,cansymbol from {} order by (canvote) desc".format(topic)
cur.execute(query7)
result=cur.fetchall()
for row in result:
    print("The Winner Is: ",row[0].upper(),"-",row[1])
    time.sleep(1)
    print("#"*10,"CONGRAGULATIONS","#"*10)
    break
print("*"*50)
time.sleep(3)

#DELETION OF TABLE
choose=""
print("Do You Want To Delete Detalis Of Candidates(y/n)")
choose=input("ENTER YOUR CHOICE: ")
if choose.lower()=="y":
    query8="delete from {}".format(topic)
    cur.execute(query8)
    con.commit()
    print("***CANDIDATE DETAILS CLEARED***")
else:
    print("***CANDIDATE DETAILS SAVED***")
