from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

