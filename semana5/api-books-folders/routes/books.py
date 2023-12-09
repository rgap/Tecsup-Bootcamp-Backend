from flask import Blueprint, jsonify, request
from models.book import Book
from utils import response_error, response_success

books = Blueprint("books", __name__, url_prefix="/api/v1")

book = Book()


@books.route("/books", methods=["GET"])
def get_books():
    return jsonify(book.list_books())


@books.route("/books", methods=["POST"])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        book.insert_book(new_book)
        return response_success("Libro creado correctamente", 201)

    except Exception as e:
        return response_error(str(e), 500)


@books.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        searched = book.search_book_by_id(book_id)
        if not searched:
            return response_error("No se encontró el libro", 500)
        return searched
    except Exception as e:
        return response_error(str(e), 500)


@books.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        deleted = book.delete_book_by_id(book_id)
        return jsonify({"message": deleted})

    except Exception as e:
        return response_error(str(e), 500)


@books.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        data = request.get_json()
        updated_book = book.update_book_by_id(book_id, data)
        if not updated_book:
            return response_error("No se encontró el libro", 500)
        return response_success("Libro actualizado", 201)
    except Exception as e:
        return response_error(str(e), 500)
