import mysql.connector

#conect to database
conn = mysql.connector.connect(
host="localhost",
user="root",
password="Himanshu@423",
db="new_db"
)
cursor = conn.cursor()
#function to insert the data into the database
def insert_data(name,email):
    sql = "insert into user_data (name,email) values (%s, %s)"
    val = (name,email)
    cursor.execute(sql,val)
    conn.commit()
    print(cursor.rowcount, "record inserted.")

#main function
if  __name__ == "__main__":
    name = input("enter your name:")
    email = input("enter your email:")
    insert_data(name, email)

# close the connection
cursor.close()
conn.close()
