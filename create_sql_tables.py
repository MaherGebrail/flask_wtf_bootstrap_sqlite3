import sqlite3


conn= sqlite3.connect("test.db")#it create file if not exist
c=conn.cursor()


# c.execute("""CREATE TABLE users (
#         name  VARCHAR UNIQUE NOT NULL,email  VARCHAR UNIQUE NOT NULL, pass VARCHAR NOT NULL)""")

# c.execute("""INSERT INTO users(name,pass,email) VALUES (:name,:pass,:mail)""",
#           {"name":'tester',"pass":123456789,"mail":'tester@yahoo.com'})

# conn.commit()
#c.execute(""" SELECT * FROM users WHERE VALUES (name = :name,pass= :pass)""",{"name":form.username.data,"pass":form.password.data})



# print(c.execute("""SELECT * FROM users""").fetchall())

# c.execute("""DROP TABLE users""")


