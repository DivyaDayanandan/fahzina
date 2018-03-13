import MySQLdb
db=MySQLdb.connect("localhost","","","student1")
cursor=db.cursor()
cursor.execute("create table tab1(id int,Name varchar(10)")
cursor.execute("insert into tab1 values(1,'manu')")
cursor.execute("insert into tab1 values(2,'anu')")
cursor.execute("insert into tab1 values(3,'vinu')")
cursor.execute("update tab1 set name='binu',where id=3")
cursor.execute("delete from tab1 where id=1")
cursor.execute("select * from tab1")
for col in cursor.fetchall():
	print col[0],col[1]
cursor.execute("commit")
db.close()
