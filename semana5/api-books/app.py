from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from utils import response_error, response_success  # Import utility functions

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/booksdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Migrate
# migrate = Migrate(app, db)


# Model
class Book(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    description = db.Column(db.String(255))
    summary = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __init__(self, title, author, description, summary, image_url):
        self.title = title
        self.author = author
        self.description = description
        self.summary = summary
        self.image_url = image_url

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "summary": self.summary,
            "image_url": self.image_url,
        }


# Controller for Displaying Books
@app.route("/books", methods=["GET"])
def get_books():
    try:
        books = Book.query.all()
        books_data = [book.to_json() for book in books]
        return response_success(books_data, 200)
    except Exception as e:
        return response_error(str(e), 500)


# Controller for Displaying a Single Book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            return response_error("Book not found", 404)
        return response_success(book.to_json())
    except Exception as e:
        return response_error(str(e), 500)


# Controller for Creating a Book
@app.route("/books", methods=["POST"])
def create_book():
    try:
        book = Book(**request.get_json())
        db.session.add(book)
        db.session.commit()
        return response_success("Book created successfully", 201)
    except IntegrityError:
        return response_error("Book already existed")
    except Exception as e:
        return response_error(str(e), 500)


if __name__ == "__main__":
    app.run(debug=True)
