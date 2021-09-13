query4="select canname,max(canvote) from candidate"
cur.execute(query4)
result=cur.fetchall()
for row in result:
    print("the winner is: ",row[0])
    print("CONGRAGULATION")

choose=""
print("do you want to delete detalis of candidates(y/n): ")
choose=input("enter your choice")
if choose.lower()=="y":
    query5="delete from candidate"
    cur.execute(query5)
    con.commit()
    print("candidate details deleted")
else:
    print("candidate details saved")
