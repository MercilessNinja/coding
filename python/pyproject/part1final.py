import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
l2=[]
def linsearch(l,x):
    f=0
    for i in range(len(l)):
        if l[i]==x:
            f=1
            return (f)
    else:
        return (f)
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
        print(l2)
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
        query2="select * from candidate"
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
