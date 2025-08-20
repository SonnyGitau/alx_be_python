# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return a string representation of a Book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with a title, author, and file size (MB)."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """Return a string representation of an EBook."""
        return f"'{self.title}' by {self.author} [E-Book, {self.file_size} MB]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with a title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """Return a string representation of a PrintBook."""
        return f"'{self.title}' by {self.author} [Print Book, {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initialize a Library with an empty book collection."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
