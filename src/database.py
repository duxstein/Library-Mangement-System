import mysql.connector
from mysql.connector import Error

def connect_db():
    """
    Connect to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",      # MySQL server address
            user="root",           # MySQL username
            password="root",  # MySQL password
            database="library"     # Database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    
def add_book(book_id, title, author, price):
    """
    Add a new book to the database.
    """
    try:
        db = connect_db()
        if db:
            cursor = db.cursor()
            query = "INSERT INTO books (Book_ID, Book_Title, Author, Price) VALUES (%s, %s, %s, %s)"
            values = (book_id, title, author, price)

            cursor.execute(query, values)
            db.commit()
            print("Book added successfully")
            cursor.close()
            db.close()
    except Error as e:
        print(f"Error while adding book: {e}")

def close_db(connection):
    """
    Close the database connection.
    """
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")