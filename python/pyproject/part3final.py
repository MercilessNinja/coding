import time
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()

print("final list of all candidates:")
query3="select * from candidates"
cur.execute(query3)
result=cur.fetchall()
print("canNo","%18s"%"Name","%10s"%"Symbol")
for row in result:
    print(row[0],"%20s"%row[1],"%10s"%row[3])

            
l1=[0]
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
    print(time1)

print("*"*50)
             
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
        print(l1)
        while True:
            if vo_no>=1 and vo_no<=vono:
                if result==1:
                    print("***NOT ELIGIBLE TO VOTE(YOU HAVE ALREADY VOTED)***")
                    break
                elif result==0:
                    print("YOU CAN VOTE NOW")
                    print('*'*50)
                    print("CANDIDATE LIST:-")
                    query6="select * from candidate"
                    cur.execute(query6)
                    result=cur.fetchall()
                    for row in result:
                        print(row[0],".",row[1])
                    query3="select * from candidates"
                    cur.execute(query3)
                    result=cur.fetchall()
                    print("canNo","%18s"%"Name","%10s"%"Symbol")
                    for row in result:
                        print(row[0],"%20s"%row[1],"%10s"%row[3])
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
