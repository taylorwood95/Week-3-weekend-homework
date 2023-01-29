from models.book import Book


book1 = Book("A Brief History of Time", "Stephen Hawking", "Non-Fiction", True)
book2 = Book("SAS Rogue Heroes", "Ben MacIntyre", "Non-Fiction", False)
book3 = Book("When Breath Becomes Air", "Paul Kalanithi", "Non-Fiction", True)
books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)


def remove_book(remove_book):
    for book in books:
        if (
            book.title == remove_book.title
            and book.author == remove_book.author
            and book.genre == remove_book.genre
            and book.checked_out
        ):
            books.remove(book)


def return_book(index):
    new_books = []
    book = books[index]
    new_books.append(book)
    return new_books
