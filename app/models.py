from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(20), unique=True, nullable=False)  # Alphanumeric book ID
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_roll = db.Column(db.Integer, db.ForeignKey('student.student_roll'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    fine = db.Column(db.Float)

    student = db.relationship('Student', backref='transactions')
    book = db.relationship('Book', backref='transactions')
    
class Student(db.Model):
    __tablename__ = 'student'  # Explicitly set the table name to 'student'

    student_roll = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Address1 = db.Column(db.String(100), nullable=False)
    Address2 = db.Column(db.String(100))
    PostCode = db.Column(db.String(10))
    Mobile = db.Column(db.String(15))

    def __repr__(self):
        return f"<Student {self.student_roll}: {self.first_name} {self.last_name}>"