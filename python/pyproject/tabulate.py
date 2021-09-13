import pandas
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="1234",database="vote")
cur=con.cursor()
cur.execute("select * from candidates")
result=cur.fetchall()
headers=["snno","name","vote","symbol"]
l=[]
for r in result:
    l.append(r)
print(pandas.DataFrame(l,None,headers))
print()

