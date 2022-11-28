import sqlite3

# Establishing connection to database if exist else create a sample database
conn = sqlite3.connect('test.db')

# Executing Query for creation of table (If table is already created it will give existing table exist error)
# query = """create table company_5(id int primary key not null, Name text not null, age int not null, address char(50), salary real)"""
# conn.execute(query)

# Executing Query for inserting data into table (If data already present it will give existing data present error because of the same primary key value)
# query = """insert into company_5(id, name, age, address, salary) values(1,'Paul',32,'Californiqa',210546)"""
# conn.execute(query)
# conn.commit()

# Executing  Query for retrieval of data 
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY_5")
# for row in cursor:
#     print("ID = 1 ", row[0])
#     print("NAME = Paul ", row[1])
#     print("ADDRESS = 32,'California' ", row[2])
#     print("SALARY = 21040.00 ", row[3])
#     print("Operation done successfully")

# Command for deletion of a particular row and gives error if data is not present in the table
a = """DELETE FROM COMPANY_5 WHERE ID = 1"""
conn.execute(a)
# Any changes will not be reflected in the database untill we call commit
conn.commit()
print("Record delete successfully")

# After all the operations we close our connection to the database
conn.close()