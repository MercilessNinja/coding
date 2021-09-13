import time
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
l2=[]
l1=[]
def linsearch(l,x):
    f=0
    for i in range(len(l)):
        if l[i]==x:
            f=1
            return (f)
    else:
        return (f)

def voteadd(vot):
    query4="update candidates set canvote=canvote+1 where canno={}".format(vot)
    cur.execute(query4)
    con.commit()
    print("Vote Counted Successfully")
    time1=time.strftime("%I:%M:%S%p")
    print("voting time: ",time1)
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
        result=linsearch(l2,no)
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
        
print("final list of all candidates:")
query3="select * from candidates"
cur.execute(query3)
result=cur.fetchall()
print("CanNo","%18s"%"Name","%10s"%"Votes","%10s"%"Symbol")
for row in result:
    print(row[0],"%20s"%row[1],"%10s"%row[2],"%10s"%row[3])

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
             
vono=int(input("enter number of voters: "))
for i in range(1,vono+1):
    query5="insert into voters values({})".format(i)
    cur.execute(query5)
    con.commit()
n=3   
k=0
while k<vono:
    age=int(input("Enter Your Age: "))
    if age>=18:
        vo_no=int(input("Enter Voter ID: "))
        result=linsearch(l1,vo_no)
        while True:
            if vo_no>=1 and vo_no<=vono:
                if result==1:
                    print("***NOT ELIGIBLE TO VOTE(YOU HAVE ALREADY VOTED)***")
                    break
                elif result==0:
                    print("YOU CAN VOTE NOW")
                    print('*'*50)
                    print("CANDIDATE LIST:-")
                    query6="select * from candidates"
                    cur.execute(query6)
                    result=cur.fetchall()
                    for row in result:
                        print(row[0],".",row[1])
                    vot=int(input("Enter Candidate Number To Vote: "))
                    if vot<=n:
                        voteadd(vot)
                        l1.extend([vo_no])
                        print('*'*50)
                        k=k+1
                    else:
                        print("***CANDIDATE NUMBER IS INCORRECT:Vote Again***")
                    break
            else:
                print("***VOTER ID IS INVALID***")
                break
    else:
        print("##YOU ARE NOT ALLOWED TO VOTE##")

time.sleep(10)

query7="select canname from candidates order by (canvote) desc"
cur.execute(query7)
result=cur.fetchall()
for row in result:
    print("The Winner Is: ",row[0])
    print("#"*10,"CONGRAGULATIONS","#"*10)
    break

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

