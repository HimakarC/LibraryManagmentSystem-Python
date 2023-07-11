class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book '{}' by {} added to the library.".format(title, author))

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    print("Book '{}' by {} is available.".format(book.title, book.author))
                else:
                    print("Book '{}' by {} is currently borrowed.".format(book.title, book.author))
                return
        print("Book '{}' not found in the library.".format(title))

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book '{}' by {} is borrowed.".format(book.title, book.author))
                else:
                    print("Book '{}' is already borrowed.".format(book.title))
                return
        print("Book '{}' not found in the library.".format(title))

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book '{}' by {} is returned.".format(book.title, book.author))
                else:
                    print("Book '{}' is already available.".format(book.title))
                return
        print("Book '{}' not found in the library.".format(title))

library = Library()

N = int(input('Enter no.of times to ask the query: '))

for j in range(N):
    n = int(input('Enter\n 1) To add book to the Library\n 2) To search for the book\n 3) To borrow the book\n 4) To return the book\n'))

    if n == 1:
        s = input('Enter book name to add to the library: ')
        name = input('Enter author name of the book: ')
        library.add_book(s, name)
    elif n == 2:
        s = input('Enter book name to add to the library: ')
        library.search_book(s)
    elif n == 3:
        s = input('Enter book name to add to the library: ')
        library.borrow_book(s)
    else:
        s = input('Enter book name to add to the library: ')
        library.return_book(s)
