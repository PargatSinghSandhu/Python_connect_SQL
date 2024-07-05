from getpass import getpass
from mysql.connector import connect, Error

try:
    connection= connect(
    host="localhost",
    user=input("Enter Username: "),
    password=getpass("Enter Password: "),
    database="online_movie_rating"
    )
    alter_table_query = """
    ALTER TABLE movies
    MODIFY COLUMN collection_in_mil DECIMAL(5,2)"""
    
    show_table_query = "DESCRIBE movies"
    with connection.cursor() as cursor:
        cursor.execute(alter_table_query) #alter query
        cursor.execute(show_table_query)#show query
        #fetch all rows from the last executed query, everything updated results
        result=cursor.fetchall()
        print("Movie Table Schema after alteration")
        for row in result:
            print(row)
    

        
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        
