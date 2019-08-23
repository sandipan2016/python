import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (5, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (6, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (7, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (8, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (2468,'Rajiv',28,'27, D.H. Road, Behala,Kol-34',24000.90)")
conn.commit()
print("Records created successfully")
conn.close()