class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.genre})'


class Library:
    def __init__(self):
        self.books = []
        self.index = 0

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)

    def __next__(self):
        if self.index > len(self.books):
            raise StopIteration

        current_book = self.books[self.index]
        self.index += 1
        return current_book


if __name__ == '__main__':
    book1 = Book("It", "King", "horror")
    book2 = Book("The Lord of the Rings", "Tolkien", "fantasy")
    book3 = Book("The Shining", "King", "horror")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    for b in library:
        print(b)
