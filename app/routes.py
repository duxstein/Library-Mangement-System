from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User, Book, Transaction
from datetime import datetime
from app.models import Student, Book, Transaction

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database for the user
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))  # Redirect to the admin dashboard
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/admin')
def admin_dashboard():
    books = Book.query.all()
    return render_template('admin.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    price = request.form['price']

    # Check if the book_id already exists
    existing_book = Book.query.filter_by(book_id=book_id).first()
    if existing_book:
        flash('Book ID already exists. Please use a unique Book ID.', 'error')
        return redirect(url_for('admin_dashboard'))

    new_book = Book(book_id=book_id, title=title, author=author, price=price)
    db.session.add(new_book)
    db.session.commit()

    flash('Book added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/transactions')
def transactions():
    # Fetch all transactions from the database
    transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    try:
        student_roll = request.form['student_roll']
        book_id = request.form['book_id']
        issue_date = datetime.strptime(request.form['issue_date'], '%Y-%m-%d')
        return_date = datetime.strptime(request.form['return_date'], '%Y-%m-%d') if request.form['return_date'] else None
        fine = float(request.form['fine']) if request.form['fine'] else 0.0

        # Check if the student_roll exists
        student = Student.query.filter_by(student_roll=student_roll).first()
        if not student:
            flash('Invalid Student Roll Number. Please enter a valid roll number.', 'error')
            return redirect(url_for('transactions'))

        # Check if the book_id exists
        book = Book.query.filter_by(book_id=book_id).first()
        if not book:
            flash('Invalid Book ID. Please enter a valid book ID.', 'error')
            return redirect(url_for('transactions'))

        new_transaction = Transaction(
            student_roll=student.student_roll,  # Use the student's roll number from the database
            book_id=book.id,  # Use the book's ID from the database
            issue_date=issue_date,
            return_date=return_date,
            fine=fine
        )
        db.session.add(new_transaction)
        db.session.commit()

        flash('Transaction added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding transaction: {str(e)}', 'error')

    return redirect(url_for('transactions'))






@app.route('/students')
def students():
    

    # Fetch all students from the 'student' table
    students = Student.query.all()
    return render_template('students.html', students=students)