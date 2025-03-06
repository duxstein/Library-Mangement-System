from tkinter import *
from tkinter import messagebox
from database import connect_db

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database
    db = connect_db()
    if db:
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)

        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful!")
            # Open Admin Dashboard or Student Dashboard
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

        # Close the database connection
        cursor.close()
        db.close()

# Create the main window
root = Tk()
root.title("Library Management System - Login")
root.geometry("400x300")

# Username Label and Entry
label_username = Label(root, text="Username:")
label_username.pack()
entry_username = Entry(root)
entry_username.pack()

# Password Label and Entry
label_password = Label(root, text="Password:")
label_password.pack()
entry_password = Entry(root, show="*")
entry_password.pack()

# Login Button
button_login = Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()