from typing import List

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    # Borrow a book
    def borrow_book(self, book):
        self.borrowed_books.append(book)

    # Return a book
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

    # Show borrowed books
    def show_borrowed_books(self):
        if not self.borrowed_books:
            return f"{self.name} has not borrowed any books."
        res = [f"{self.name} borrowed books:"]
        for b in self.borrowed_books:
            res.append(b.show_info())
        return "\n".join(res)
