class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self._isbn = isbn          
        self._is_available = True
        

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self._isbn

    def is_available(self):
        return self._is_available

    # Set loan status
    def set_available(self, status: bool):
        self._is_available = status

    # Show book info
    def show_info(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"ISBN: {self._isbn} Title: {self.title} Author: {self.author} Status: {status}"
