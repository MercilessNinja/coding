from tkinter import *
from PIL import ImageTk,Image
import pandas
import time
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
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

def voteadd(vot):#FUNCTION FOR ADDING VOTES
    query4="update candidates set canvote=canvote+1 where canno={}".format(vot)
    cur.execute(query4)
    con.commit()
    print("Vote Counted Successfully")
    time1=time.strftime("%I:%M:%S%p")
    print("voting time: ",time1)


def buttonfunc():#COMMAND FOR BUTTON1 IN TKINTER
    cur.execute("select * from candidates")
    result=cur.fetchall()
    headers=["snno","name","vote","symbol"]
    l=[]
    for r in result:
        l.append(r)
    print(pandas.DataFrame(l,None,headers))
    print()

def buttonf():#COMMAND FOR BUTTON2 IN TKINTER
    print("you can vote now")

topic=input("ENTER VOTING NAME: ")
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
            query1="insert into candidates values({},'{}',{},'{}')".format(no,name,vote,symbol)
            cur.execute(query1)
            con.commit()
            print("***CANDIDATE DETAILS ADDED***")
            a+=1
            time.sleep(1)
    elif choice==2:
        query2="select * from candidates"
        cur.execute(query2)
        result=cur.fetchall()
        print("canNo","%18s"%"Name","%10s"%"Votes")
        for row in result:
            print(row[0],"%20s"%row[1],"%10s"%row[2])
    elif choice==0:
        con.close()
        print("bye!!")
    else:
        print("***INVALID CHOICE***")

time.sleep(3)
#DISPLAYING LIST OF CANDIDATES        
print("Final List Of All Candidates:")
cur.execute("select * from candidates")
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
        query="select * from candidates where canno={}".format(num)
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
                query="update CANDIDATES set canname='{}',cansymbol='{}' where canno={}".format(d,s,num)
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
#VERIFICATION OF VOTERS
cur.execute("select count(canno) from candidates")
result=cur.fetchall()
for v in result:
    p=v[0]
    break
k=0
while k<vono:
    age=int(input("Enter Your Age: "))
    if age>=18:
        vo_no=int(input("Enter Voter ID: "))
        result=linsearch(l1,vo_no)#USEAGE OF LINEAR SEARCH
        while True:
            if vo_no>=1 and vo_no<=vono:
                if result==1:
                    print("***NOT ELIGIBLE TO VOTE(YOU HAVE ALREADY VOTED)***")
                    break
                elif result==0:
                    print("YOU CAN VOTE NOW")
                    print('*'*50)
                    window=Tk()
                    window.title('voting')
                    window.geometry('400x500')
                    l=Label(window,text="WELCOME TO VOTING SESSION")
                    l.pack()
                    lab=Label(window,text=topic)
                    lab.pack()
                    img=ImageTk.PhotoImage(Image.open("voting.png"))
                    mylabel=Label(image=img)
                    mylabel.pack()
                    b=Button(window,text="click to view candidates",command=buttonfunc)#USAGE OF FUNCTION BUTTONFUNC
                    b.pack()
                    b1=Button(window,text="click me!!",command=buttonf)#USAGE OF FUNCTION BUTTONF
                    b1.pack()
                    lab1=Label(window,text="click exit to continue voting:")
                    lab1.pack()
                    quiet=Button(window,text='exit',command=window.destroy)
                    quiet.pack()
                    window.mainloop()
                    vot=int(input("Enter Candidate Number To Vote: "))
                    if vot<=p:
                        voteadd(vot)#USAGE OF FUNCTION VOTEADD
                        l1.extend([vo_no])
                        time.sleep(1)
                        print('*'*50)
                        time.sleep(1)
                        k=k+1
                    else:
                        print("***CANDIDATE NUMBER IS INCORRECT:Vote Again***")
                        time.sleep(1)
                    break
            else:
                print("***VOTER ID IS INVALID***")
                time.sleep(1)
                break
    else:
        print("##YOU ARE NOT ALLOWED TO VOTE##")
        time.sleep(1)
print("CALCULATING VOTES...")

time.sleep(5)
#DECLARATION OF WINNER
query7="select canname,cansymbol from candidates order by (canvote) desc"
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
    query8="delete from candidates"
    cur.execute(query8)
    con.commit()
    print("***CANDIDATE DETAILS CLEARED***")
else:
    print("***CANDIDATE DETAILS SAVED***")




