from getpass import getpass
from mysql.connector import connect, Error

try:
    connection= connect(
    host="localhost",
    user=input("Enter Username: "),
    password=getpass("Enter Password: "),
    database="online_movie_rating"
    )
    #didn't add id because it is auto increamental
    insert_movies_query = """
    INSERT INTO movies (title, release_year, genre, collection_in_mil)
    VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9),
    ("Casablanca", 1942, "Romance", 1.0),
    ("Avengers: Endgame", 2019, "Action", 858.8),
    ("Night of the Living Dead", 1968, "Horror", 2.5),
    ("The Godfather", 1972, "Crime", 135.6),
    ("Haider", 2014, "Action", 4.2),
    ("Inception", 2010, "Adventure", 293.7),
    ("Evil", 2003, "Horror", 1.3),
    ("Toy Story 4", 2019, "Animation", 434.9),
    ("Air Force One", 1997, "Drama", 138.1),
    ("The Dark Knight", 2008, "Action",535.4),
    ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
    ("The Lion King", 1994, "Animation", 423.6),
    ("Pulp Fiction", 1994, "Crime", 108.8),
    ("Kai Po Che", 2013, "Sport", 6.0),
    ("Beasts of No Nation", 2015, "War", 1.4),
    ("Andadhun", 2018, "Thriller", 2.9),
    ("The Silence of the Lambs", 1991, "Crime", 68.2),
    ("Deadpool", 2016, "Action", 363.6),
    ("Drishyam", 2015, "Mystery", 3.0)
"""
    
    show_table_query = "DESCRIBE movies"
    
    with connection.cursor() as cursor:
    #we write the commands in the above section, then we execute below what we need to do
        cursor.execute(insert_movies_query) #alter query
        connection.commit()
        
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
        
