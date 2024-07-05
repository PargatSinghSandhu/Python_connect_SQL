from getpass import getpass
from mysql.connector import connect, Error

try:
    connection= connect(
    host="localhost",
    user=input("Enter Username: "),
    password=getpass("Enter Password: "),
    database="online_movie_rating"
    )


    
    with connection.cursor() as cursor:
    #we write the commands in the above section, then we execute below what we need to do
       
        
        cursor.execute("SELECT * FROM movies") #seelct all movie records from movie table
        movies = cursor.fetchall() #fetch and print all movie records
        print("\n Movies Table Data")
        for movie in movies:
            print(movie)
        
    

        
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        
