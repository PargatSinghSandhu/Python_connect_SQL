from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating", //here you are connecting to exisiting db
    ) as connection:
        with connection.cursor() as cursor:
            print(connection)
except Error as e:
    print(e)

