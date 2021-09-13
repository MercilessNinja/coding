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

def count(n):#FUNCTION TO COUNT VOTE
    global k
    cur.execute("update {} set canvote=canvote+1 where canno={}".format(topic,n))
    con.commit()
    k=k+1
    l1.extend([int(b)])
    
def finish():#FUNCTION TO VERIFY CANDIDATE NUMBER 
    global root6
    global c
    c=ent.get()
    button5.config(state=DISABLED)
    label10=Label(root5,text="##PLEASE CLOSE THIS WINDOW##").pack()
    while int(c)<=m and int(c)>0:
        root6=Tk()
        root6.title("confirmation")
        root6.geometry("250x100")
        label11=Label(root6,text="DO YOU WANT TO CONFIRM??")
        label11.grid(row=0,column=0)
        button6=Button(root6,text="YES",fg="white",bg="green",command=lambda:[count(c), root6.destroy()])
        button6.grid(row=0,column=1)
        button7=Button(root6,text="NO",fg="white",bg="red",command=root6.destroy)
        button7.grid(row=0,column=2)
        root6.mainloop()
        break
    else:
        label12=Label(root5,text="**INVALID CANDIDATE NUMBER**").pack()

def idfication():#FUNCTION TO VERIFY VOTER ID
    global b
    global result
    global root4
    global root5
    global button5
    global ent
    b=g.get()
    button2.config(state=DISABLED)
    result=linsearch(l1,int(b))
    labuul=Label(root2,text="##PLEASE CLOSE THIS WINDOW##").pack()
    if result==1:
        root4=Tk()
        root4.geometry("300x300")
        root4.title("verification result")
        label4=Label(root4,text="**NOT ELIGIBLE(ALREADY VOTED FROM THIS ID)**").pack()
        button4=Button(root4,text="EXIT",command=root4.destroy,bg="black",fg="white")
        button4.pack()
        root4.mainloop()
    if result==0 and int(b)<=vono and int(b)>=1:
        root5=Tk()
        root5.title("casting vote")
        root5.geometry("600x900")
        label5=Label(root5,text="CANDIDATE LIST:-").pack()
        cur.execute("select * from {}".format(topic))
        res=cur.fetchall()
        for v in res:
            label6=Label(root5,text=str(v[0])+'-'+v[1]+"\t("+v[3]+")").pack()
        label7=Label(root5,text="ENTER CANDIDATE NUMBER:").pack()
        ent=Entry(root5, width=30)
        ent.pack()
        button5=Button(root5,text="NEXT->",command=lambda:[finish()],bg="black",fg="white")
        button5.pack()
        root5.mainloop()
    elif int(b)>vono or int(b)<1:
        label8=Label(root2,text="**INCORRECT VOTER ID**").pack()
        
def age():#FUNCTION TO VERIFY AGE
    global a
    global g
    global button2
    global root2
    a=e.get()
    button1.config(state=DISABLED)
    lubul=Label(root1,text="##PLEASE CLOSE THIS WINDOW##").pack()
    if int(a)>=18:
        root2=Tk()
        root2.geometry("300x300")
        root2.title("id verification")
        label2=Label(root2,text="ENTER VOTER ID:").pack()
        g=Entry(root2, width=30)
        g.pack()
        button2=Button(root2,text="NEXT->",command=lambda:[idfication()],bg="black",fg="white")
        button2.pack()
        root2.mainloop()
    else:
        label9=Label(root1,text="##PLEASE CLOSE THIS WINDOW##").pack()
        root3=Tk()
        lablel3=Label(root3,text="**YOU CANNOT VOTE(UNDERAGE)**").pack()
        button3=Button(root3,text="EXIT",command=lambda:[root3.destroy()],bg="black",fg="white")
        button3.pack()
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
        print("Proceeding...")
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
                s = (input("ENTER NEW SYMBOL,(LEAVE BLANK IF NOT WANT TO CHANGE):  "))
                if s=="":
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
cur.execute("select count(canno) from {}".format(topic))
r=cur.fetchall()
for i in r:
    m=i[0]
    break
 
h=0
l=0
b=""
a=""
k=0
while k<vono:
    root1=Tk()
    root1.geometry("300x300")
    root1.title("age verification")
    label1=Label(root1,text="Enter Your Age:").pack()
    e=Entry(root1, width=30)
    e.pack()
    button1=Button(root1,text="NEXT->",command=lambda:[age()],bg="black",fg="white")
    button1.pack()
    root1.mainloop()

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
