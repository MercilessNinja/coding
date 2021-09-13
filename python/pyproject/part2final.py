import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
print("##CANDIDATE UPDATION##")
ans='y'
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
                d=row[2]
            try:
                s = (input("ENTER NEW SYMBOL,(LEAVE BLANK IF NOT WANT TO CHANGE):  "))
            except:
                s=row[3]
            query="update CANDIDATES set canname='{}',cansymbol='{}' where canno={}".format(d,s,num)
            cur.execute(query)
            con.commit()
            print("## RECORD UPDATED ## ")
    ans=input("UPDATE MORE (y/n) :")
            
