from tkinter import *
from database import connect_db

def add_book():
    book_id = entry_book_id.get()
    title = entry_title.get()
    author = entry_author.get()
    price = entry_price.get()

    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO books (Book_ID, Book_Title, Author, Price) VALUES (%s, %s, %s, %s)"
    values = (book_id, title, author, price)

    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Book Added Successfully!")

# Admin Dashboard GUI
root = Tk()
root.title("Admin Dashboard")
root.geometry("600x400")

# Add Book Section
label_book_id = Label(root, text="Book ID:")
label_book_id.pack()
entry_book_id = Entry(root)
entry_book_id.pack()

label_title = Label(root, text="Title:")
label_title.pack()
entry_title = Entry(root)
entry_title.pack()

label_author = Label(root, text="Author:")
label_author.pack()
entry_author = Entry(root)
entry_author.pack()

label_price = Label(root, text="Price:")
label_price.pack()
entry_price = Entry(root)
entry_price.pack()

button_add_book = Button(root, text="Add Book", command=add_book)
button_add_book.pack()

root.mainloop()