from getpass import getpass
from mysql.connector import connect, Error

try:
    connection= connect(
    host="localhost",
    user=input("Enter Username: "),
    password=getpass("Enter Password: "),
    database="online_movie_rating"
    )
    
    show_table_query = "DESCRIBE movies"
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        #fetch all rows from the last executed query, everything updated results
        result=cursor.fetchall()
        for row in result:
            print(row)
    

        
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        
