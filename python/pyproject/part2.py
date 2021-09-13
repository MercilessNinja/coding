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
    query1="update candidate set canvote=canvote+1 where canno={}".format(vot)
    cur.execute(query1)
    con.commit()
    print("voted successfully")
             
vono=int(input("enter number of voters"))
for i in range(1,vono+1):
    query2="insert into voters values({})".format(i)
    cur.execute(query2)
    con.commit()
    
k=0
while k<vono:
    vo_no=int(input("enter voter id"))
    result=linsearch(l1,vo_no)
    print(l1)
    while True:
        if vo_no>=1 and vo_no<=vono:
            if result==1:
                print("you cannot vote")
                break
            elif result==0:
                print(" you can vote")
                l1.extend([vo_no])
                query3="select * from candidate"
                cur.execute(query3)
                result=cur.fetchall()
                for row in result:
                    print(row[0],".",row[1])
                vot=int(input("enter candidate number to vote"))
                if vot<=n:
                    voteadd(vot)
                    k=k+1
                else:
                    print("candidate number incorrect")
                break
        else:
            print("invalid")
            break
