from getpass import getpass
from mysql.connector import connect, Error

try:
    connection= connect(
    host="localhost",
    user=input("Enter Username: "),
    password=getpass("Enter Password: "),
    database="online_movie_rating"
    )
    
    create_movies_table_query="""
    CREATE TABLE movies
    (id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT)
    """
    
    with connection.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        connection.commit
        print("Movies table created succesfully")
        
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        
