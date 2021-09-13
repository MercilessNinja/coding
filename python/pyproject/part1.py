import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
a=0
choice=None
n=int(input("enter number of candidates"))
while choice!=0 and a<n:
    print("1.ADD CANDIDATE")
    print("2.SHOW CANDIDATE")
    print("0.EXIT")
    choice=int(input("enter your choice"))
    if choice==1:
        no=int(input("enter candidate number"))
        name=input("enter candidate name")
        vote=0
        query="insert into candidate values({},'{}',{})".format(no,name,vote)
        cur.execute(query)
        con.commit()
        print("candidate added")
        a+=1
    elif choice==2:
        query="select * from candidate"
        cur.execute(query)
        result=cur.fetchall()
        print("canNo","%20s"%"Name","%10s"%"Votes")
        for row in result:
            print(row[0],"%20s"%row[1],"%10s"%row[2])
    elif choice==0:
        con.close()
        print("bye!!")
    else:
        print("***INVALID CHOICE***")
print("final list of all candidates:")
query="select * from candidate"
cur.execute(query)
result=cur.fetchall()
print("canNo","%20s"%"Name","%10s"%"Votes")
for row in result:
    print("{:<5}{:<10}{:<5}").format(row[0],row[1],row[2])
