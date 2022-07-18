import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Octavia67",
    database="dany"
)
if(db):
    print("Connection Successful")
else:
    print("No connection")
crsr = db.cursor()

# 0. pip install mysql-connector-python
# 1. crsr.execute("CREATE DATABASE dany")
# 2. add database="dany" to db = mysql.connector.connect()
# 3. crsr.execute("CREATE TABLE Persons (PersonID int, LastName varchar(255))")
# 4. crsr.execute("INSERT INTO persons (ID, Fname, Lname) VALUES (2, 'Marina', 'Goralkin')")
# OR
# 4. person = [id, fn, ln]
# 4. crsr.execute("INSERT INTO persons (ID, Fname, Lname) VALUES (%s, %s, %s)", person)
# OR
# 4. crsr.executemany() => persons = [(id, fn, ln), (id, fn, ln)]
# Commit Changes
# 5. db.commit()
# To Read:
# 6. Use fetchall(), fetchmany(), and fetchone() methods of a cursor class to fetch all or limited rows from a table.
# 7. crsr.execute("SELECT * FROM persons")
# 8. read = crsr.fetchall()


id = 5
fn = "Mia"
ln = "Goralkin"
person = [id, fn, ln]
# crsr.execute("INSERT INTO persons (ID, Fname, Lname) VALUES (%s, %s, %s)", person)
# db.commit()


crsr.execute("SELECT * FROM persons")
read = crsr.fetchall()
len = len(read[0])

for row in read:
    for x in range(len):
        print(row[x], end = ' ')
    print("")

