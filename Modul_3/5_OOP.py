class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    # @title.setter
    # def title(self, value):
    #     self.__title = value

    @property
    def author(self):
        return self.__author

    # @author.setter
    # def author(self, value):
    #     self.__author = value

    def __str__(self):
        return f'{self.__title} - {self.__author}'


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        for v in self.__books:
            print(v)


class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.file_size = size

    def __str__(self):
        return f'{super().__str__()} (размер файла: {self.file_size} МБ'
lib = Library()

book1 = Book('Война и мир', 'Л. Толстой')
book2 = EBook('Пайтон для начинающих', 'Иван Петров', 5)
# print(book1)
# print(book2)
lib.add_book(book1)
lib.add_book(book2)

lib.show_books()