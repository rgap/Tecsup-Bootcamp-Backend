from utils import generate_id


class Book:
    books = []

    def __init__(
        self,
        title=None,
        isbn=None,
        author=None,
        description=None,
        summary=None,
        image_url=None,
    ):
        self.id = id(isbn)
        self.title = title
        self.isbn = isbn
        self.author = author
        self.description = description
        self.summary = summary
        self.image_url = image_url

    def list_books(self):
        return [item.to_json() for item in self.books]

    def search_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_book_by_id(self, book_id):
        book_searched = self.search_book(book_id)
        if book_searched is not None:
            return book_searched.to_json()
        return None

    def insert_book(self, book):
        book.id = generate_id(self.books)
        self.books.append(book)

    def delete_book_by_id(self, book_id):
        book_searched = self.search_book(book_id)
        try:
            self.books.remove(book_searched)
            return "Eliminado correctamente"
        except Exception as e:
            return "No se encontró el libro"

    def update_book_by_id(self, book_id, book_data):
        book_searched = self.search_book(book_id)
        if book_searched is not None:
            book_searched.title = book_data.get("title", book_searched.title)
            book_searched.isbn = book_data.get("isbn", book_searched.title)
            book_searched.author = book_data.get("author", book_searched.title)
            book_searched.description = book_data.get(
                "description", book_searched.title
            )
            book_searched.summary = book_data.get("summary", book_searched.title)
            book_searched.image_url = book_data.get("image_url", book_searched.title)
            return book_searched.to_json()
        return None

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn,
            "author": self.author,
            "description": self.description,
            "summary": self.summary,
            "image_url": self.image_url,
        }
